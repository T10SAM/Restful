import os
from dotenv import load_dotenv
from pathlib import Path

# Garante que o .env seja carregado do diretório correto
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")

#if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
#    raise EnvironmentError("Uma ou mais variáveis de ambiente não foram carregadas.")
