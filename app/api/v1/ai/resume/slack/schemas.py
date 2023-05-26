# schemas.py
from typing import List,Optional
from fastapi import Form
from pydantic import BaseModel, Field

class SlackCommand(BaseModel):
    token: str = Form(...)
    team_id: str = Form(...)
    team_domain: str = Form(...)
    channel_id: str = Form(...)
    channel_name: str = Form(...)
    user_id: str = Form(...)
    user_name: str = Form(...)
    command: str = Form(...)
    text: str = Form(...)
    response_url: str = Form(...)
