import torch
from transformers import pipeline
from fastapi import FastAPI

device = "cuda:0" if torch.cuda.is_available() else "cpu"
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-small",
    chunk_length_s=30,
    device=device,
)

from src.app.router import router as transcription_router


app = FastAPI()
app.include_router(transcription_router)
