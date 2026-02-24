import numpy as np
import ffmpeg
import torch
import torchaudio
import io
from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from .models import Transcription
from database import SessionLocal
from main import pipe

router = APIRouter(prefix="/transcription", tags=["Transcription"])


def load_audio(audio_data):
    audio_file = io.BytesIO(audio_data)
    speech_array, sampling_rate = torchaudio.load(audio_file)
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(
            orig_freq=sampling_rate, new_freq=16000
        )
        speech_array = resampler(speech_array)
    # Ensure the audio is 1D vector
    if speech_array.ndim > 1:
        speech_array = torch.mean(speech_array, dim=0)

    return speech_array, 16000


@router.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    db = SessionLocal()

    try:
        while True:
            data = await websocket.receive_bytes()
            if not data:
                continue
            speech_array, sampling_rate = load_audio(data)

            result = pipe(speech_array)

            transcribed_text = result.get("text", "")
            word_count = len(transcribed_text.split())
            duration_seconds = len(speech_array) / sampling_rate

            db_entry = Transcription(
                transcription_text=transcribed_text,
                word_count=word_count,
                duration_seconds=round(duration_seconds, 2),
            )
            db.add(db_entry)
            db.commit()
            db.refresh(db_entry)

            await websocket.send_json(
                {
                    "id": db_entry.id,
                    "transcription_text": db_entry.transcription_text,
                    "word_count": db_entry.word_count,
                    "duration": db_entry.duration_seconds,
                }
            )

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Server Error: {e}")
    finally:
        db.close()
