from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "html" in response.text.lower()

def test_get_pokemon_found():
    response = client.get("/pikachu")
    assert response.status_code == 200
    assert "Pikachu" in response.text or "pikachu" in response.text

def test_get_pokemon_not_found():
    response = client.get("/noexistepokemon123")
    assert response.status_code == 200  # Devuelve el template de home
    assert "html" in response.text.lower()