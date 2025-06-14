from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    nome: str
    email: str
    idade: int

class UserCreate(UserBase):
    senha: str

class UserUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    idade: Optional[int] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
