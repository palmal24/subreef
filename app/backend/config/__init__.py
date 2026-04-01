from .settings import Settings

settings = Settings()

settings.AUDIO_FILES_DIR.mkdir(parents=True, exist_ok=True)
settings.BUNDLE_DIR.mkdir(parents=True, exist_ok=True)