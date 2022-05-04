import requests
from django.core.management.base import BaseCommand
from recipes.models import Recipe

def get_data():
    #setup the http request
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q=dinner&app_id=5e46e2fc&app_key=73242337544cac1a326435a7ab5bec29'
    r = requests.get(url, headers={'Content-Type':      
    'application/json'})
    #save the json respone into variable
    recipe = r.json()
    #return the json
    return recipe['hits']

def seed_data():
    for item in get_data():
        recipe = Recipe(
            name = item["recipe"]["label"]
        )

        recipe.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_data()
        print("seeding completed")

