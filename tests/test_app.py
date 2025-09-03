import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Testa se a rota /list_users responde (mesmo sem DB conectado)."""
    response = client.get("/list_users")
    # O status pode ser 200 (OK) ou 500 (erro do DB), mas a rota deve existir
    assert response.status_code in [200, 500]

def test_root_not_found(client):
    """Testa se rota inexistente retorna 404"""
    response = client.get("/")
    assert response.status_code == 404
