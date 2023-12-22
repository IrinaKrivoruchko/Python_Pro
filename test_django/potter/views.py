from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingredients, Elixirs, Houses, Spells
from .serializers_potter import IngredientsSerializer, ElixirsSerializer, HousesSerializer, SpellsSerializer

class IngredientsViews(viewsets.ModelViewSet):
    serializer_class = IngredientsSerializer
    queryset = Ingredients.objects.order_by('identifier')


class ElixirsViews(viewsets.ModelViewSet):
    serializer_class = ElixirsSerializer
    queryset = Elixirs.objects.order_by('identifier')

class HousesViews(viewsets.ModelViewSet):
    serializer_class = HousesSerializer
    queryset = Houses.objects.order_by('name')

class SpellsViews(viewsets.ModelViewSet):
    serializer_class = SpellsSerializer
    queryset = Spells.objects.order_by('name')