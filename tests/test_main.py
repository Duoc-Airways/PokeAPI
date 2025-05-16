"""Tests for main FastAPI app."""

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home_page():
    """Test home page loads successfully."""
    response = client.get("/")
    assert response.status_code == 200
    assert "html" in response.text.lower()


def test_get_pokemon_found():
    """Test getting a known Pokémon returns a page."""
    response = client.get("/pikachu")
    assert response.status_code == 200
    assert "pikachu" in response.text.lower()


def test_get_pokemon_not_found():
    """Test getting an unknown Pokémon returns home page."""
    response = client.get("/noexistepokemon123")
    assert response.status_code == 200
    assert "html" in response.text.lower()
