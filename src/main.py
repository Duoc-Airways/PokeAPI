from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

templates = Jinja2Templates(directory='html')

@app.get('/home/{pokemon_name}')
async def get_pokemon(request: Request, pokemon_name: str):
    result = get_pokemon_info(pokemon_name)
    name = result["name"]
    heigth = result["height"]
    weight = result["weight"]
    abilities = result["abilities"]
    types = result["types"]
    sprites = result["sprites"]

    return templates.TemplateResponse('home.html', {"request": request, "name": name, "types": types, "sprites": sprites})

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "sprites": pokemon_data["sprites"]["front_default"]
        }
        return pokemon_info
    else:
        return None