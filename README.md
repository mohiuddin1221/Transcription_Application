# AI Audio Transcription Application

A real-time audio transcription service built with **FastAPI**, **WebSockets**, and **HuggingFace Whisper Model**. This application allows users to upload audio files via WebSockets and receive instant text transcriptions, which are also stored in a database.

## 🚀 Features
* **Real-time Transcription:** Uses WebSockets for low-latency communication.
* **Whisper AI:** Powered by OpenAI's Whisper model for high-accuracy speech-to-text.
* **Database Integration:** Automatically saves transcriptions, word counts, and audio duration.
* **Audio Processing:** Built-in resampling to 16kHz and mono-channel conversion using `torchaudio`.

## 🛠️ Tech Stack
* **Backend:** FastAPI (Python)
* **AI Model:** HuggingFace Transformers (Whisper)
* **Audio Engine:** Torchaudio
* **Database:** SQLAlchemy 
* **Client:** Vanilla JavaScript (WebSocket API)

## 📋 Prerequisites
Before running the project, ensure you have the following installed:
* Python 3.9+

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohiuddin1221/Transcription_Application.git
   cd Transcription_Application

2. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate 
    On Windows: venv\Scripts\activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the Server:**
    ```bash
    uvicorn main:app --reload
