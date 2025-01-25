'''
An API (Application Programming Interface) is a set of rules that allows one piece of software to interact with another. 
It enables communication between different systems, like a browser and a web server.
python -m venv venv - Windows
python3 -m venv venv - Mac

venv\Scripts\activate - Windows
source venv/bin/activate - Mac

pip install requests
pip3 install requests
pip3 freeze > requirements.txt

'''
import requests
import json
import pprint
# pikachu
def get_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}') 

    if response.status_code == 200:
        data = response.json()
        # pprint.pp(data)
        print(type(data))
    else:
        print(f"Error: {response.status_code} {response._content}")

    print(f"Pokemon Name: {data['name']}")
    print(f"Pokemon Weight: {data["weight"]}")
    poke_types = data["types"]
    for idx, types in enumerate(poke_types):
        print(f"{idx + 1}. {types["type"]["name"]}")
    

# get_pokemon('charizard')

def get_cat():
    headers = {'x-api-key': '<YOUR KEY>'}
    response = requests.get("https://api.thecatapi.com/v1/images/search", headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)
        # pprint.pp(data)
        # print(type(data))
    else:
        print(f"Error: {response.status_code} {response._content}")

# get_cat()

# def test(param1, param2, param3):
#     print(param1, param2, param3)

# test(param2="There", param3="General Kenobi", param1="Hello")

def get_access_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type" : 'client_credentials',
              "client_id": '<YOUR ID>',
              'client_secret': '<YOUR SECRET>'}
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        # pprint.pp(data)
        # print(type(data))
    else:
        print(f"Error: {response.status_code} {response._content}")
    
    return data['access_token']

token = get_access_token()
# print(token)

def get_playlist(t):
    print(t)
    headers = {'Authorization' : "Bearer " + t}
    response = requests.get("https://api.spotify.com/v1/users/turbospudz/playlists", headers=headers)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        pprint.pp(data)
        # print(type(data))
    else:
        print(f"Error: {response.status_code} {response._content}")

get_playlist(token)