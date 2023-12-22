from rest_framework import serializers
from .models import Ingredients, Elixirs, Houses, Spells
class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ['identifier', 'name']

class ElixirsSerializer(serializers.ModelSerializer):
    # ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Elixirs
        fields = ['identifier', 'name']

class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ['identifier', 'name', 'houseColours', 'founder', 'animal', 'element']

class SpellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spells
        fields = ['identifier', 'name']