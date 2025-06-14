from typing import List
from core.logging_config import logger
from sqlalchemy.orm import Session
from models.users import User
from schemas.user_schema import UserCreate, UserUpdate
from datetime import datetime
from core.auth_utils import get_password_hash


def create_user(db: Session, user: UserCreate) -> User:
    logger.info(f"Creating user: {user.email}")
    hashed_password = get_password_hash(user.senha)
    db_user = User(
        nome=user.nome,
        email=user.email,
        idade=user.idade,
        senha=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#Buscar todos os usuários
def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()


#Buscar o usuário pelo id
def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, user_email: str) -> User | None:
    return db.query(User).filter(User.email == user_email).first()


#Atualizar um usuário
def update_user(db: Session, user_id: int, user: UserUpdate) -> User | None:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    for field, value in user.dict(exclude_unset=True).items():
        setattr(db_user, field, value)
    db_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True
