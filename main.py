from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from controller import user_controller, task_controller
from core.database import Base, engine
from core.logging_config import logger
import logging

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Instância principal do app
app = FastAPI(
    title="API de Tarefas Colaborativas",
    version="1.0.0",
    description="Projeto educacional com FastAPI + MySQL"
)

# Registrar os routers
app.include_router(user_controller.router)
app.include_router(task_controller.router)

#Registro de logs no terminal
logging.basicConfig(
    level=logging.INFO,  # Pode ser DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

#Tratamento de erros possiveis
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    logger.warning(f"IntegrityError: {exc.orig} | URL: {request.url}")
    return JSONResponse(
        status_code=409,
        content={"detail": "Violação de integridade do banco de dados. Verifique duplicidade ou dados inválidos."}
    )

@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"SQLAlchemyError: {exc} | URL: {request.url}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Erro interno ao acessar o banco de dados."}
    )