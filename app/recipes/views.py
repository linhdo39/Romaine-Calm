from tokenize import String
from unicodedata import name
from django.http import HttpRequest, HttpResponse
import os
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, Favorite, Ingredients, UserRecipe
import requests
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

# Create your views here.

def all_view(request):
    if "search" in request.GET:
        recipe_list = Recipe.objects.order_by('?')[:20]
        search = request.GET["search"]
        #url = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=" + APP_ID+ "&app_key="+APP_KEY
        recipe_list = Recipe.objects.all().filter(name__contains = search)
        return render(request, "recipes/findRecipe.html", {'recipe_list': recipe_list})
    else:
        recipe_list = Recipe.objects.order_by('?')[:20]
        return render(request, "recipes/findRecipe.html", {'recipe_list': recipe_list})

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


def add_recipe_view(request):
    if request.method == 'POST':
        userRecipe = UserRecipe (
            name = request.POST.get('Title'),
            category = request.POST['category'],
            recipe_photo = request.FILES['recipephoto'],
            ingredient = request.POST.get('Ingredients'),
            total_hours = request.POST.get('totalhrs'),
            total_mins = request.POST.get('totalmins'),
            description = request.POST.get('Subhead'),
            preparation = request.POST.get('instructions'),
            author = request.user.username
        )
        userRecipe.save()

        recipe = Recipe (
            name = request.POST.get('Title'),
            recipe_id = request.user.id,
            category = request.POST['category'],
            userRecipe = True      
        )
        recipe.save()

        return render(request, "recipes/userRecipe.html", {'recipe': userRecipe})
    else:
        return render(request, "pages/addUserRecipe.html", {})

def my_recipe_view(request):
    list = UserRecipe.objects.filter(user = request.user.username)
    return render(request, "recipes/myRecipe.html", {'recipe': list})

def edit_recipe_view(request,id):
    if request.method == 'POST':
        UserRecipe.objects.get_or_create(id)
        userRecipe = UserRecipe (
            name = request.POST.get('Title'),
            category = request.POST['category'],
            recipe_photo = request.FILES['recipephoto'],
            ingredient = request.POST.get('Ingredients'),
            total_hours = request.POST.get('totalhrs'),
            total_mins = request.POST.get('totalmins'),
            description = request.POST.get('Subhead'),
            preparation = request.POST.get('instructions'),
            author = request.user.username
        )
        userRecipe.save()

        recipe = Recipe (
            name = request.POST.get('Title'),
            recipe_id = request.user.id,
            category = request.POST['category'],
            userRecipe = True      
        )
        recipe.save()

        return render(request, "recipes/userRecipe.html", {'recipe': userRecipe})
    else:
        userRecipe = UserRecipe.objects.get_or_create(id)
        return render(request, "pages/addUserRecipe.html", {"userRecipe":userRecipe})