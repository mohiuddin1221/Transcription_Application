from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database import Base

class Transcription(Base):
    __tablename__ = "transcriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    transcription_text: Mapped[str] = mapped_column(String)
    word_count: Mapped[int] = mapped_column(Integer)
    duration_seconds: Mapped[float] = mapped_column(Float)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)