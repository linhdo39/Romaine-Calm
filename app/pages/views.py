from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HOMEPAGE
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>HomePage</h1>")


#TEST CAN BE REMOVED FOR PRODUCTION

def help_view(*args, **kwargs):
    return HttpResponse("THIS IS THE HELP PAGE")