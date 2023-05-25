from pydantic import BaseSettings
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    #Project
    PROJECT_NAME: str = "FastAPI Project Chat Resume"
    PROJECT_VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    #DB
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_NAME: str = os.getenv("MONGODB_NAME", "test")

    #JWT config
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")

class Channels_settings(BaseSettings):
    #Channels
    SLACK_TOKEN = os.environ.get("SLACK_TOKEN")

class OPENAI_settings(BaseSettings):
    #Channels
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

settings = Settings()
channels_settings= Channels_settings()
openai_settings = OPENAI_settings()
