from django.core.management.base import BaseCommand
from potter.models import Ingredients
import requests
import json

URL_POTTER = 'https://wizard-world-api.herokuapp.com/'
URL_Ingredients = URL_POTTER + 'ingredients'

class Command(BaseCommand):
    help_text = 'Команда для заповнення БД'

    def handle(self, *args, **options):
        print('Start')
        request_ingredients = requests.get(URL_Ingredients)
        all_ingredients = json.loads(request_ingredients.text)
        for item in all_ingredients:
            Ingredients.objects.get_or_create(
            identifier = item['id'],
            name = item['name'],)

        print('Finish')


