from django.core.management.base import BaseCommand
from potter.models import Elixirs
import requests
import json

URL_POTTER = 'https://wizard-world-api.herokuapp.com/'
URL_Elixirs = URL_POTTER + 'elixirs'

class Command(BaseCommand):
    help_text = 'Команда для заповнення БД'

    def handle(self, *args, **options):
        print('Start')
        request_elixirs = requests.get(URL_Elixirs)
        all_elixirs = json.loads(request_elixirs.text)
        for item in all_elixirs:
            Elixirs.objects.get_or_create(
            identifier = item['id'],
            name = item['name'],)

        print('Finish')