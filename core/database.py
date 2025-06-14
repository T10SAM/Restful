import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core import config

logger = logging.getLogger(__name__)

database_url = f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"
engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Teste a conexão

def get_db():
    db = SessionLocal()
    try:
        logger.info("Conectado ao banco de dados!")
        yield db
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        db.close()