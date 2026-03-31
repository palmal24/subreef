from fastapi import APIRouter
from fastapi.responses import RedirectResponse


router_home = APIRouter()

@router_home.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")