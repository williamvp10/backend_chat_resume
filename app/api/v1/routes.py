from fastapi import APIRouter

#ai
from app.api.v1.ai.resume.slack.routes import router as ai_resume_slack_router

api_router = APIRouter()

#ai
api_router.include_router(ai_resume_slack_router, prefix="/ai/slack", tags=["AI resume slack"])


@api_router.get("/", response_model=dict)
async def home():
    return {"name":"api chat resume AI"}