from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class TaskPriority(str, Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class StatusEnum(str, Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: TaskPriority
    status: StatusEnum
    parent_id: Optional[int] = None
    workspace_id: int

class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    priority: TaskPriority
    status: StatusEnum
    created_by_id: int
    assignee_id: Optional[int] = None
    parent_id: Optional[int] = None
    workspace_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None


class TaskFilter(BaseModel):
    status: Optional[StatusEnum] = None
    priority: Optional[TaskPriority] = None
    assignee_id: Optional[int] = None
    reported_by: Optional[int] = None
    workspace_id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None
    status: Optional[StatusEnum] = None
    assignee_id: Optional[int] = None
    parent_id: Optional[int] = None