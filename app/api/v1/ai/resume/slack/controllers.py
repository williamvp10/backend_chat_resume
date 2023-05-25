from app.db.mongodb import get_db
from pymongo.collection import Collection, ObjectId
from fastapi import HTTPException
from .schemas import SignCreate

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from app.core.config import channels_settings
from app.services.openia.resume import generate_general_resume

slack_token = channels_settings.SLACK_TOKEN
client = WebClient(token=slack_token)

async def get_channel_summary(channel_id: str):
    try:
        print(channel_id)
        response = client.conversations_history(channel=channel_id)
        print(response)
        messages = response["messages"]
        #text = "\n".join("{}:{}".format(message['user'],message['text']) for message in messages)
        users, chatresume_id = get_users_info(messages)
        return {"resume": await generate_general_resume(messages, users, chatresume_id)}
    except SlackApiError as e:
        return {"error": str(e)}
    

def get_users_info(messages):
    users = {}
    chatresume_id=""
    for message in messages:
        user_id = message.get('user')
        if user_id and user_id not in users:
            try:
                response = client.users_info(user=user_id)
                users[user_id] = response['user']
                if users[user_id]['name']=="chatresume":
                    chatresume_id=users[user_id]['id']
            except SlackApiError as e:
                print(f"Error obtaining info for user {user_id}: {e}")
    print(users)
    return users, chatresume_id