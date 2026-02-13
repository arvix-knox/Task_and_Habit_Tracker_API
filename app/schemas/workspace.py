from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class Role(str, Enum):
    owner = 'owner'
    admin = 'admin'

class WorkspaceCreate(BaseModel):
    name: str
    key: str
    description: str | None = None

class WorkspaceResponse(BaseModel):
    id: int
    name: str
    key: str
    description: str  | None = None
    created_at: datetime

class WorkspaceMember(BaseModel):
    workspace_id: int
    user_id: int
    role: str


class WorkspaceMemberRead(BaseModel):
    user_id: int
    username: str
    email: str
    role: Role
    joined_at: datetime


# Примерный путь для использования в коде: "/workspaces/{workspace_id}/invite"
class InviteCreate(BaseModel):
    workspace_id: int
    email: EmailStr
    role: Role


