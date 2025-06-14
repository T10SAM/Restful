import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    # Cria um usuário antes, se necessário
    user_data = {"nome": "Teste", "email": "teste@exemplo.com", "idade": 30, "senha": "123456"}
    client.post("/users/", json=user_data)
    # Cria uma tarefa
    task_data = {
        "nome": "Tarefa Teste",
        "descricao": "Descrição",
        "task_status": "pendente",
        "prazo": "2025-12-31T23:59:59",
        "id_users": 1
    }
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    assert response.json()["nome"] == "Tarefa Teste"

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_export_user_tasks_csv():
    response = client.get("/tasks/user/1/export")
    assert response.status_code in (200, 404)  # Pode não haver tarefas para o usuário
    if response.status_code == 200:
        assert response.headers["content-type"].startswith("text/csv")

def test_update_task():
    update_data = {"nome": "Tarefa Atualizada"}
    response = client.put("/tasks/1", json=update_data)
    assert response.status_code in (200, 404)

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code in (204, 404)
