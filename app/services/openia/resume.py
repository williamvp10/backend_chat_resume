# gpt.py
import openai
import asyncio
import os
import json
from app.core.config import openai_settings

# Load the environment variables from the .env file
OPENAI_API_KEY = openai_settings.OPENAI_API_KEY

async def generate_general_resume(messages, users, chatresume_id, aditional_text="") -> dict:
     # Combina todos los mensajes en un solo texto
    chat = "\n".join(f"{users[message['user']]['real_name']}: {message['text']}" for message in messages if 'user' in message and message['user'] != chatresume_id)

    # Añade la información de los usuarios al prompt
    user_info = "\n".join("{}: {{ real_name: {}, is_admin: {} }}".format(user['name'],user['real_name'],user['is_admin']) for user in users.values())
    #print(user_info)
    prompt = f"The following is a conversation from a Slack channel.\nThe participants are:\n\n{user_info}\nthe chat is:\n{chat}\n\nAs an AI language model, your task is to provide a detailed summary that encapsulates the key points, decisions, and action items from this conversation.give me the summary in spanish. ignore messages starting with /summarize. {aditional_text}"
    #print(prompt)
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.8
        )
    
    #print(response)
    #falta validar si si hay choices y si hay contenido en json 
    response_text:str = str(response.choices[0].text)
    #response_text=response_text.replace('\n','')
    return response_text

