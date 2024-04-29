from functools import lru_cache

from app.settings import Settings
from fastapi import APIRouter, Depends
from typing_extensions import Annotated


@lru_cache
def get_settings():
    return Settings()


router = APIRouter(
    prefix="/api/legislator",
    tags=["legislators"],
    responses={404: {"description": "not found"}},
)


@router.get("/")
async def get_legislators(settings: Annotated[Settings, Depends(get_settings)]):
    return {"legislator": []}
