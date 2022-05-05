from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index_view(response):
    #return HttpResponse("recipe home")
    return render(response, "recipes/home.html", {})
