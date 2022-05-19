from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HOMEPAGE
def homepage_view(response):
    #return HttpResponse("<h1>HomePage</h1>")
    return render(response, "pages/home.html", {})


def profile_view(response):
    return render(response, "pages/Favorite.html", {})

def about_view(response):
    return render(response, "pages/soon.html", {})

def news_view(response):
    return render(response, "pages/soon.html", {})

def contact_view(response):
    return render(response, "pages/soon.html", {})

def add_recipe_view(response):
    return render(response, "pages/AddUserRecipe.html", {})

#TEST CAN BE REMOVED FOR PRODUCTION

def help_view(response):
    return render(response, "pages/soon.html", {})