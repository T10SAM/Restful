from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user_schema import UserCreate, UserUpdate, UserResponse
from repositories import user_repository
from core.database import get_db
from typing import List

router = APIRouter(prefix = "/users", tags = ["users"])

#Criar Usuário
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = user_repository.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return user_repository.create_user(db, user)

#Listar todos os usuários
@router.get("/", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_repository.get_all_users(db)

#Buscar usuário por ID
@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = user_repository.get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Atualizar Usuário
@router.put("/{id}", response_model=UserResponse)
def update_user(id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated = user_repository.update_user(db, id, user_update)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

#Deletar Usuário
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
    deleted = user_repository.delete_user(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    