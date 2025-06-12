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

    class Config: #Diz ao Pydantic para aceitar objetos ORM, permitindo retornar instâncias da Task diretamente nas rotas sem convertê-las manualmente.
        orm_mode = True