import requests
from django.core.management.base import BaseCommand
from recipes.models import Recipe
from recipes.info import APP_ID
from recipes.info import APP_KEY

#remember to install python requests
def get_data():
    id = APP_ID
    key = APP_KEY
    #setup the http request
    url = 'https://api.edamam.com/api/recipes/v2?type=public&beta=true&q=all&app_id=' + id+ '&app_key='+key
    r = requests.get(url, headers={'Content-Type':      
    'application/json'})
    #save the json respone into variable
    recipe = r.json()
    #return the json
    return recipe['hits']

def seed_data():
    items = get_data()
    for item in items:
        uri = item["recipe"]["uri"]
        uri = uri.replace("http://www.edamam.com/ontologies/edamam.owl#recipe_","")
        recipe = Recipe (
            name = item["recipe"]["label"],
            recipe_id = uri         
        )

        recipe.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_data()
        print("seeding completed")

