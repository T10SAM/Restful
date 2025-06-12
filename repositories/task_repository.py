from typing import List
from sqlalchemy.orm import Session
from models.tasks import Task
from schemas.task_schema import  TaskCreate, TaskUpdate
from datetime import datetime

def create_task(db: Session, task: TaskCreate) -> Task:
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#Buscar todas as tasks
def get_all_tasks(db: Session) -> List[Task]:
    return db.query(Task).all()

#Buscar uma task pelo id
def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()

#Buscar uma task pelo id do usuário
def get_task_by_userid(db: Session, user_id: int) -> Task | None:
    return db.query(Task).filter(Task.id_users == user_id).all()

#Atualizar uma task existente
def update_task(db: Session, task_id: int ,task: TaskUpdate) -> Task | None:
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return None
    for field, value in task.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    db_task.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int) -> bool:
    db_task = get_task_by_id(db, task_id)
    if not db_task:
        return False
    db.delete(db_task)
    db.commit()
    return True