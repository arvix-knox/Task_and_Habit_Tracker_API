from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


