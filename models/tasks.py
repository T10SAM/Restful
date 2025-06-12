from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from core.database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    descricao = Column(String(100))
    task_status = Column(String(100), default="pendente")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    prazo = Column(DateTime, default=datetime.utcnow)
    id_users = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Task(id={self.id}, nome='{self.nome}', status='{self.task_status}')>"