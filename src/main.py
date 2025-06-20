"""Main FastAPI app for Pokédex search and display."""

from fastapi import FastAPI, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='FrontEnd')


@app.get('/')
def home_page(request: Request):
    """Render the home page template."""
    return templates.TemplateResponse('home/home.html', {"request": request})


@app.get('/{pokemon_name}')
async def get_pokemon(request: Request, pokemon_name: str):
    """Render the Pokémon page or return 404 if not found."""
    result = get_pokemon_info(pokemon_name)
    if result is None:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    name = result["name"]
    height = result["height"]
    weight = result["weight"]
    abilities = result["abilities"]
    types = result["types"]
    sprites = result["sprites"]
    return templates.TemplateResponse(
        'pokemon/pokemon.html',
        {
            "request": request,
            "name": name,
            "types": types,
            "abilities": abilities,
            "height": height,
            "weight": weight,
            "sprites": sprites
        }
    )


def get_pokemon_info(pokemon_name):
    """Fetch Pokémon info from the PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        pokemon_data = response.json()
        type_styles = {
            "normal": {"color": "#A8A77A", "emoji": "⚪"},
            "fire": {"color": "#EE8130", "emoji": "🔥"},
            "water": {"color": "#6390F0", "emoji": "💧"},
            "electric": {"color": "#F7D02C", "emoji": "⚡"},
            "grass": {"color": "#7AC74C", "emoji": "🌿"},
            "ice": {"color": "#96D9D6", "emoji": "❄️"},
            "fighting": {"color": "#C22E28", "emoji": "🥊"},
            "poison": {"color": "#A33EA1", "emoji": "☠️"},
            "ground": {"color": "#E2BF65", "emoji": "🌍"},
            "flying": {"color": "#A98FF3", "emoji": "🕊️"},
            "psychic": {"color": "#F95587", "emoji": "🔮"},
            "bug": {"color": "#A6B91A", "emoji": "🐛"},
            "rock": {"color": "#B6A136", "emoji": "🪨"},
            "ghost": {"color": "#735797", "emoji": "👻"},
            "dragon": {"color": "#6F35FC", "emoji": "🐉"},
            "dark": {"color": "#705746", "emoji": "🌑"},
            "steel": {"color": "#B7B7CE", "emoji": "⚙️"},
            "fairy": {"color": "#D685AD", "emoji": "🧚"}
        }
        types = [
            {
                "name": type_data["type"]["name"],
                "color": type_styles[type_data["type"]["name"]]["color"],
                "emoji": type_styles[type_data["type"]["name"]]["emoji"]
            }
            for type_data in pokemon_data["types"]
        ]
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [
                ability["ability"]["name"]
                for ability in pokemon_data["abilities"]
            ],
            "types": types,
            "sprites": pokemon_data["sprites"]["front_default"]
        }
        return pokemon_info
    return None


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(
    request: Request, exc: StarletteHTTPException
):
    """Handle HTTP exceptions with custom 404 page."""
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "errors/404.html", {"request": request}, status_code=404
        )
    return await http_exception_handler(request, exc)
