import requests, os
from dotenv import load_dotenv

load_dotenv() # load .env file to retrieve api key

# api info
api_key = os.getenv("API_KEY")
url = "https://api.coingecko.com/api/v3/simple/price"
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": f"{api_key}"
}

"""Representation of a crypto coin."""
class Crypto:
    def __init__(self, name:str):
        self.name = name

        params = {
            "ids": name,
            "vs_currencies": "usd"
        }

        response = requests.get(url, headers=headers, params=params)
        status_code = response.status_code

        if status_code == 200:
            data = response.json()
        else:
            data = None

        self.price=data[self.name]["usd"]
        
    
    def get_name(self):
        return self.name

    
    def get_price(self):
        return self.price
    