from django.core.management.base import BaseCommand
from potter.models import Spells
import requests
import json

URL_POTTER = 'https://wizard-world-api.herokuapp.com/'
URL_Spells = URL_POTTER + 'spells'

class Command(BaseCommand):
    help_text = 'Команда для заповнення БД'

    def handle(self, *args, **options):
        print('Start')
        request_spells = requests.get(URL_Spells)
        all_spells = json.loads(request_spells.text)
        for item in all_spells:
            Spells.objects.get_or_create(
            identifier = item['id'],
            name = item['name'],
            )

        print('Finish')