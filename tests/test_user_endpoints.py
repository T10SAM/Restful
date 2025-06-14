import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    user_data = {"nome": "Usuário Teste", "email": "usuario@teste.com", "idade": 25, "senha": "senha123"}
    response = client.post("/users/", json=user_data)
    assert response.status_code in (201, 400)  # Pode já existir

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code in (200, 404)

def test_update_user():
    update_data = {"nome": "Usuário Atualizado"}
    response = client.put("/users/1", json=update_data)
    assert response.status_code in (200, 404)

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code in (204, 404)
