from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from repositories import task_repository, user_repository
from core.database import get_db
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

#Criar nova tarefa
@router.post("/", response_model = TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    user = user_repository.get_user_by_id(db, task.id_users)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return task_repository.create_task(db, task)

#Listar todas as tarefas
@router.get("/", response_model=List[TaskResponse])
def list_tasks(db:Session = Depends(get_db)):
    return task_repository.get_all_tasks(db)

#Buscar tarefa por ID
@router.get("/{id}", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)):
    task = task_repository.get_task_by_id(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

#Listar todas as tarefas atribuídas a um usuário
@router.get("/user/{id_users}", response_model=List[TaskResponse])
def get_user_tasks(id_users: int, db: Session = Depends(get_db)):
    return task_repository.get_task_by_userid(db, id_users)

#Atualizar a tarefa
@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = task_repository.update_task(db, id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

#Deletar tarefa
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, db: Session = Depends(get_db)):
    deleted = task_repository.delete_task(db, id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")