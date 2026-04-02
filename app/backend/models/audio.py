from pydantic import BaseModel


class AudioResponse(BaseModel):
    message: str
    status_code: int

class AudioFile(BaseModel):...