from django.http import HttpRequest, HttpResponse
import os
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, FavoriteRecipe#, Ingredients
import requests
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

# Create your views here.

def all_view(response):
    recipe_list = Recipe.objects.order_by('?')[:20]
    return render(response, "recipes/findRecipe.html", {'recipe_list': recipe_list})

def index_view(response,id):
    #return HttpResponse("recipe home")
    url = "https://api.edamam.com/api/recipes/v2/" + id+"?type=public&app_id=" + APP_ID + "&app_key="+ APP_KEY
    r = requests.get(url, headers={'Content-Type':      
    'application/json'})
    recipe = r.json()   
    output = {
        "uri": recipe["recipe"]["uri"],
        "name":recipe["recipe"]["label"],
        "image":recipe["recipe"]["image"],
        "yield":recipe["recipe"]["yield"],
        "ingredients":recipe["recipe"]["ingredientLines"],
        "instruction":recipe["recipe"]["url"],
    }
    return render(response, "recipes/individualRecipe.html", {'recipe': output})

def favorite_view(response,id):
    favorite_list = FavoriteRecipe.objects.get(id)
    return render(response, "pages/favorite.html", {'favorite_list': favorite_list})

'''def ingredient_view(response,id):
    ingredient_list = Ingredients.objects.get(id)
    return render(response, "pages/ingredients.html", {'ingredient_list': ingredient_list})

def add_ingredient(response,id):
    ingredient_list = Ingredients.objects.get(id)
    return render(response, "pages/ingredients.html", {'ingredient_list': ingredient_list})'''