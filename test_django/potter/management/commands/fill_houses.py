from django.core.management.base import BaseCommand
from potter.models import Houses
import requests
import json

URL_POTTER = 'https://wizard-world-api.herokuapp.com/'
URL_Houses = URL_POTTER + 'houses'

class Command(BaseCommand):
    help_text = 'Команда для заповнення БД'

    def handle(self, *args, **options):
        print('Start')
        request_houses = requests.get(URL_Houses)
        all_houses = json.loads(request_houses.text)
        for item in all_houses:
            Houses.objects.get_or_create(
            identifier = item['id'],
            name = item['name'],
            houseColours = item['houseColours'],
            founder = item['founder'],
            animal = item['animal'],
            element = item['element'],
            )

        print('Finish')


