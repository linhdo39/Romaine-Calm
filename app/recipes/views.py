from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, FavoriteRecipe
from recipes.info import APP_ID
from recipes.info import APP_KEY
import requests
# Create your views here.

def all_view(response):
    #return HttpResponse("recipe home")
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
    return render(response, "pages/Favorite.html", {'favorite_list': favorite_list})
