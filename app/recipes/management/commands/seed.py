import requests
from django.core.management.base import BaseCommand
from recipes.models import Recipe
from recipes.info import APP_ID
from recipes.info import APP_KEY

#remember to install python requests
def get_data(url):
   
    #setup the http request
    r = requests.get(url, headers={'Content-Type':      
    'application/json'})
    #save the json respone into variable
    recipe = r.json()
    #return the json
    return recipe

def seed_data():
    categories = ["breakfast", "dinner", "dessert", "lunch","brunch"]
    for category in categories:
        url = "https://api.edamam.com/api/recipes/v2?type=public&q="+category+"&app_id=" + APP_ID+ "&app_key="+APP_KEY
        items = get_data(url)
        for i in range (0, 10):
            for item in items["hits"]:
                uri = item["recipe"]["uri"]
                uri = uri.replace("http://www.edamam.com/ontologies/edamam.owl#recipe_","")
                recipe = Recipe (
                    name = item["recipe"]["label"],
                    recipe_id = uri,
                    category = category       
                )

                recipe.save()
            items = get_data(items["_links"]["next"]["href"])

class Command(BaseCommand):
    def handle(self, *args, **options):
        seed_data()
        print("seeding completed")

