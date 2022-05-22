from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HOMEPAGE
def homepage_view(response):
    #return HttpResponse("<h1>HomePage</h1>")
    return render(response, "pages/home.html", {})


def profile_view(response):
    return render(response, "pages/myprofile.html", {})


def favorite_view(response):
    return render(response, "pages/favorite.html", {})

def about_view(response):
    return render(response, "pages/soon.html", {})

def news_view(response):
    return render(response, "pages/soon.html", {})

def contact_view(response):
    return render(response, "pages/soon.html", {})

def add_recipe_view(response):
    return render(response, "pages/addUserRecipe.html", {})

#TEST CAN BE REMOVED FOR PRODUCTION

def help_view(response):
    return render(response, "pages/soon.html", {})