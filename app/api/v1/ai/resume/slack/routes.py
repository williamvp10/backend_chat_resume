from fastapi import APIRouter, Depends
from . import controllers
from .schemas import SignCreate

router = APIRouter()

@router.get("/slack/summary/{channel_id}")
async def get_channel_summary(channel_id: str):
    return await controllers.get_channel_summary(channel_id)
