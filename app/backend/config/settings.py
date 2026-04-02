from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # FastApi(uvicorn) setup
    APP_NAME: str
    HOST: str
    PORT: int

    # Files dir
    BUNDLE_DIR: Path = Path("./app/bundles")

    # Supported languages
    en: str = "English"
    es: str = "Spanish"
    fr: str = "French"
    de: str = "German"
    it: str = "Italian"
    pt: str = "Portuguese"
    ru: str = "Russian"
    zh: str = "Chinese"
    ja: str = "Japanese"
    ko: str = "Korean"
    ar: str = "Arabic"
    hi: str = "Hindi"
    nl: str = "Dutch"
    sv: str = "Swedish"
    no: str = "Norwegian"
    da: str = "Danish"
    fi: str = "Finnish"
    pl: str = "Polish"
    tr: str = "Turkish"
    cs: str = "Czech"
    el: str = "Greek"
    he: str = "Hebrew"
    th: str = "Thai"
    vi: str = "Vietnamese"
    id: str = "Indonesian"
    ro: str = "Romanian"
    hu: str = "Hungarian"
    bg: str = "Bulgarian"
    sk: str = "Slovak"
    sl: str = "Slovenian"
    hr: str = "Croatian"
    sr: str = "Serbian"
    uk: str = "Ukrainian"
    ms: str = "Malay"
    bn: str = "Bengali"
    ta: str = "Tamil"
    te: str = "Telugu"
    mr: str = "Marathi"
    kn: str = "Kannada"
    ml: str = "Malayalam"
    pa: str = "Punjabi"
    gu: str = "Gujarati"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()