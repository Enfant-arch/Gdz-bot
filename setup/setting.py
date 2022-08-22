import json
import asyncio
def load_token():
    with open("setup\src\cfg.json", "r+") as file:
        token = json.load(file)
        return str(token["Token"])



