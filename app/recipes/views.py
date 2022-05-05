from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from .models import Recipe

# Create your views here.

def index_view(response):
    #return HttpResponse("recipe home")
    recipe_list = Recipe.objects.all()
    return render(response, "recipes/home.html", {'recipe_list': recipe_list})