from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index_view(*args, **kwargs):
    return HttpResponse("recipe home")
