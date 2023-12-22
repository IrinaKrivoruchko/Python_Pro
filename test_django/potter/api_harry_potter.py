import requests
import json

URL_POTTER = 'https://wizard-world-api.herokuapp.com/'
URL_Elixirs = URL_POTTER + 'elixirs'
URL_Houses = URL_POTTER + 'houses'
URL_Ingredients = URL_POTTER + 'ingredients'
URL_Spells = URL_POTTER + 'spells'

def get_elixirs():
    request_elixirs = requests.get(URL_Elixirs)
    all_elixirs = json.loads(request_elixirs.text)
    output_elixirs = []
    for item in all_elixirs:
        data = {}
        data['id'] = item['id']
        data['name'] = item['name']
        output_elixirs.append(data)

    my_elixirs_json = json.dumps(output_elixirs)
    return my_elixirs_json

def get_houses():
    request_houses = requests.get(URL_Houses)
    all_houses = json.loads(request_houses.text)
    output_houses = []
    for item in all_houses:
        data = {}
        data['id'] = item['id']
        data['name'] = item['name']
        output_houses.append(data)

    my_houses_json = json.dumps(output_houses)
    return my_houses_json

def get_ingredients():
    request_ingredients = requests.get(URL_Ingredients)
    all_ingredients = json.loads(request_ingredients.text)
    output_ingredients = []
    for item in all_ingredients:
        data = {}
        data['identifier'] = item['id']
        data['name'] = item['name']
        output_ingredients.append(data)

    my_ingredients_json = json.dumps(output_ingredients)
    return my_ingredients_json

def get_spells():
    request_spells = requests.get(URL_Spells)
    all_spells = json.loads(request_spells.text)
    output_spells = []
    for item in all_spells:
        data = {}
        data['id'] = item['id']
        data['name'] = item['name']
        output_spells.append(data)

    my_spells_json = json.dumps(output_spells)
    return my_spells_json


# get_elixirs()
# get_houses()
get_ingredients()
# get_spells()
