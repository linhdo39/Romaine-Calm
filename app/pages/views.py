from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HOMEPAGE
def homepage_view(response):
    #return HttpResponse("<h1>HomePage</h1>")
    return render(response, "pages/home.html", {})


#TEST CAN BE REMOVED FOR PRODUCTION

def help_view(response):
    return HttpResponse("THIS IS THE HELP PAGE", {})