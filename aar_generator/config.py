from functools import lru_cache
from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel


class Settings(BaseModel):
    app_env: str = "development"
    openai_api_key: str | None = None
    openai_model: str = "auto"
    mock_llm: bool = True


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@lru_cache
def get_settings() -> Settings:
    load_dotenv()
    return Settings(
        app_env=getenv("APP_ENV", "development"),
        openai_api_key=getenv("OPENAI_API_KEY") or None,
        openai_model=getenv("OPENAI_MODEL", "auto"),
        mock_llm=_as_bool(getenv("MOCK_LLM"), True),
    )
