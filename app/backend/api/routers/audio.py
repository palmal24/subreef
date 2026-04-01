from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from services.audio import AudioService


router_audio = APIRouter(prefix="/audio")

@router_audio.post()
async def upload_audio(file: UploadFile = File(...)):
    file_bytes = await file.read()
    message, status_code = AudioService(file=file_bytes).process_audio()

    return JSONResponse(
        content={"message": message},
        status_code=status_code
    )