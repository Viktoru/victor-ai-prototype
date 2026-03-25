"""Application configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Victor_AppConfig:
    """Stores configuration values required by the application."""

    victor_openai_api_key: str
    victor_model_name: str = "gpt-4o-mini"
    victor_app_title: str = "Class One Victor AI"



def victor_get_config() -> Victor_AppConfig:
    """Load application settings from environment variables.

    Raises:
        RuntimeError: If the OpenAI API key is missing.
    """

    victor_openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not victor_openai_api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Add it to your .env file before starting the app."
        )

    victor_model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

    return Victor_AppConfig(
        victor_openai_api_key=victor_openai_api_key,
        victor_model_name=victor_model_name,
    )
