from django.contrib import admin
from .models import Ingredients, Elixirs, Houses, Spells

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name']
    search_fields = ['name']

class ElixirsAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name']
    search_fields = ['name']

class HousesAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name', 'houseColours', 'founder', 'animal', 'element']
    search_fields = ['name', 'founder', 'animal', 'element']

class SpellsAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'name']
    search_fields = ['name']


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Elixirs, ElixirsAdmin)
admin.site.register(Houses, HousesAdmin)
admin.site.register(Spells, SpellsAdmin)
