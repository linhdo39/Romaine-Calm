from tokenize import String
from django.http import HttpRequest, HttpResponse
import os
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, Favorite, Ingredients
import requests
#from dotenv import load_dotenv
#load_dotenv()

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

def favorite_view(response):
    list = Favorite.objects.filter(user = response.user.id)
    favorite_list=[]
    for item in list:
        id = item.recipe_id
        url = "https://api.edamam.com/api/recipes/v2/" + id+"?type=public&app_id=" + APP_ID + "&app_key="+ APP_KEY
        r = requests.get(url, headers={'Content-Type':      
        'application/json'})
        recipe = r.json()   
        if 'status' in recipe:
            return render(response, "pages/favorite.html",{'favorite_list': favorite_list})
        output = {
            "uri": recipe["recipe"]["uri"],
            "name":recipe["recipe"]["label"],
            "image":recipe["recipe"]["image"],
            "yield":recipe["recipe"]["yield"],
            "ingredients":recipe["recipe"]["ingredientLines"],
            "instruction":recipe["recipe"]["url"],
        }
        favorite_list.append(output)
    return render(response, "pages/favorite.html", {'favorite_list': favorite_list})

def ingredient_view(request):
    ingredient_list = Ingredients.objects.filter(user = request.user.id)
    return render(request, "recipes/ingredients.html", {'ingredient_list': ingredient_list})

def add_ingredient(request):
    ingredient_list = Ingredients.objects.filter(user = request.user.id)
    if request.POST.get('name') and request.POST.get('amount'):
        ingredient = Ingredients (
            user =  request.user,
            ingredient_name= request.POST.get('name'),
            ingredient_quantity= request.POST.get('amount')
        )
        ingredient.save()
        ingredient_list = Ingredients.objects.filter(user = request.user.id)
        return render(request, 'recipes/addIngredient.html',{'ingredient_list': ingredient_list})  
    else:
        return render(request,'recipes/addIngredient.html', {'ingredient_list': ingredient_list})
