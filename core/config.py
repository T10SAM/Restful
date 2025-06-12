import os
from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv(find_dotenv())

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

#if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
 #   raise EnvironmentError("Uma ou mais variáveis de ambiente não foram carregadas.")