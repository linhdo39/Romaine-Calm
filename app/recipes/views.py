from tokenize import String
from unicodedata import category, name
from django.http import HttpRequest, HttpResponse
import os
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe, Favorite, Ingredients, UserRecipe
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

# Create your views here.

def all_view(request):
    if "search" in request.GET:
        recipe_list = Recipe.objects.order_by('?')[:20]
        search = request.GET["search"]
        if(request.GET["primaryrecipecategory"] == '0'):
            recipe_list = Recipe.objects.all().filter(name__contains = search)
        else:
            categories = {"1": "breakfast","2": "brunch","3": "lunch","4": "dinner","5": "dessert"}
            #url = "https://api.edamam.com/api/recipes/v2?type=public&q=" + search + "&app_id=" + APP_ID+ "&app_key="+APP_KEY
            recipe_list = Recipe.objects.all().filter(name__contains = search, category=categories[request.GET["primaryrecipecategory"]])
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
    if 'json_message' in recipe or 'status' in recipe:
        return render(response, "pages/error.html",{})
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
        if 'json_message' in recipe or 'status' in recipe:
            return render(response, "pages/error.html",{})
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
    almost_expire = Ingredients.objects.filter(user = request.user.id).filter(expiration_date__month = datetime.date.today().month)
    ingredient_list = Ingredients.objects.filter(user = request.user.id).exclude(expiration_date__month = datetime.date.today().month)
    return render(request, "recipes/ingredients.html", {'ingredient_list': ingredient_list, 'almost_expire':almost_expire})

def add_ingredient(request):
    ingredient_list = Ingredients.objects.filter(user = request.user.id)
    if request.POST.get('name') and request.POST.get('amount'):
        ingredient_list = Ingredients.objects.filter(user = request.user.id).filter(ingredient_name = request.POST.get('name'))
        if ingredient_list:
            Ingredients.objects.filter(user = request.user.id).filter(ingredient_name = request.POST.get('name')).update(ingredient_quantity = request.POST.get('amount'))
            Ingredients.objects.filter(user = request.user.id).filter(ingredient_name = request.POST.get('name')).update(expiration_date = request.POST.get('expiration_date'))
        else:
            ingredient = Ingredients (
                user =  request.user,
                ingredient_name= request.POST.get('name'),
                ingredient_quantity= request.POST.get('amount'),
                expiration_date = request.POST.get('expiration_date')
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
    list = UserRecipe.objects.filter(author = request.user.username)
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