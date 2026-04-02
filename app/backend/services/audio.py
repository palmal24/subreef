from pathlib import Path
from config.settings import settings
from models.audio import AudioResponse

class AudioService:
    def __init__(self, file: bytes, filename: str):
        self.file = file
        self.filename = filename
        self.settings = settings

    def process_audio(self) -> AudioResponse:
        path: Path = self._save_audio_file()
        return AudioResponse(file_path=str(path))

    def _save_audio_file(self) -> Path:
        self.settings
        file_path = self.settings.AUDIO_FILES_DIR / self.filename
        with open(file_path, "wb") as f:
            f.write(self.file)
        return file_path

    def _process_subtitles(self, filname):...
    def _process_languages(self, target_language):...