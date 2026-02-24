import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database import Base, DATABASE_URL

from src.app.models import Transcription

load_dotenv()

config = context.config


config.set_main_option("sqlalchemy.url", DATABASE_URL)



target_metadata = Base.metadata

# run_migrations_online

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            compare_type=True
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()