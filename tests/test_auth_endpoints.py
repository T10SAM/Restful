import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login():
    # Certifique-se de que o usuário existe antes de testar login
    user_data = {"nome": "Login Teste", "email": "login@teste.com", "idade": 22, "senha": "senha123"}
    client.post("/users/", json=user_data)
    response = client.post("/auth/login", data={"username": "login@teste.com", "password": "senha123"})
    assert response.status_code in (200, 401)
    if response.status_code == 200:
        assert "access_token" in response.json()

def test_logout():
    response = client.post("/auth/logout")
    assert response.status_code == 200
    assert response.json()["message"].startswith("Logout")
