# schemas.py
from typing import List,Optional
from pydantic import BaseModel, Field

class SignCreate(BaseModel):
    zodiac_sign: str = Field(..., example="Tauro")
    type_horoscope: str  = Field(..., example="day | week | month | year")
    date: str = Field(..., example="2023-05-01 | format YYYY-MM-DD")
    language: str = Field(..., example="Spanish")
    focus_topics: str = Field(..., example="financial life, work and love")
 