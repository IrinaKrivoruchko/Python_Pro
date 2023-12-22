import requests

URL = 'http://127.0.0.1:8000/api/ingredients/?format=json'

def return_ingredients():
    req = requests.get(URL)
    print(req.status_code)
    if req.status_code == 200:
        for item in req.json():
            print(item)

return_ingredients()