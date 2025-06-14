from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    task_status: Optional[str] = "PENDENTE"
    prazo: Optional[datetime]

class TaskCreate(TaskBase):
    id_users: int #FK de usuário

class TaskUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    task_status: Optional[str] = None
    prazo: Optional[datetime] = None

class TaskResponse(TaskBase):
    id: int
    id_users: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
