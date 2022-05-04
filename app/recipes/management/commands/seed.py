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
        recipe = Recipe (
            name = item["recipe"]["label"],
            recipe_url = item["recipe"]["uri"],
            image_url = item["recipe"]["image"],
            ingredient = item["recipe"]["ingredientLines"],
            calories = item["recipe"]["calories"],
            total_time = item["recipe"]["totalTime"],
            cuisine = item["recipe"]["cuisineType"],
            mealType = item["recipe"]["mealType"],
            dishType = item["recipe"]["dishType"]
        )

        recipe.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_data()
        print("seeding completed")

