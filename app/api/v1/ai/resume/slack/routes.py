from fastapi import APIRouter, Depends, Request, BackgroundTasks
from typing_extensions import Annotated
from . import controllers
from .schemas import SlackCommand
from typing import Optional

router = APIRouter()

@router.get("/summary/{channel_id}")
async def get_channel_summary(channel_id: str):
    return await controllers.get_channel_summary(channel_id)

@router.post("/command")
async def slack_command(background_tasks: BackgroundTasks, request: Request):
    form = await request.form()
    command = SlackCommand(**form)
    #print(command.command)
    if command.command == "/summarize":
        # Aquí es donde llamarías a tu función para obtener el resumen del canal
         # Respuesta inmediata a Slack
        response = {"response_type": "in_channel", "text": "Estoy trabajando en tu resumen, te lo enviaré pronto."}
        
        # Inicia el procesamiento en segundo plano
        background_tasks.add_task(controllers.get_channel_summary_command, command)
        
        return response