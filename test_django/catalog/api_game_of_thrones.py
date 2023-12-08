import requests

URL_books = 'https://anapioficeandfire.com/api/books'

def get_books():
    req = request.get(URL_books)
    print(req)
