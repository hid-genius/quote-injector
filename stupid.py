import requests
import json


print("woooow")

def get_quote():
    print('omgomg')
    response = requests.get("https://api.kanye.rest/")
    quote = response.text
    
    print(quote)


get_quote()