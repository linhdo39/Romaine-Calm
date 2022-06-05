from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from recipes.models import Favorite
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from .forms import EditProfileForm
from recipes.models import Recipe
import requests
import os

from dotenv import load_dotenv
load_dotenv()
APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
# Create your views here.

# HOMEPAGE
def homepage_view(request):
    if request.method == 'POST' and 'like.x' in request.POST:
        favorite = Favorite(
            user = request.user,
            recipe_id = request.POST['submit']
        )
        favorite.save()
        return redirect("home")
        #return render(request, "pages/home.html", {'recipe' : output, 'r' : recipe}) 
    else:
        recipe = Recipe.objects.order_by('?')[0]
        id = recipe.recipe_id
        url = "https://api.edamam.com/api/recipes/v2/" + id + "?type=public&app_id=" + APP_ID + "&app_key="+ APP_KEY
        r = requests.get(url, headers={'Content-Type':      
        'application/json'})
        recipeJson = r.json() 
        output = {
            "uri": recipeJson["recipe"]["uri"],
            "name":recipeJson["recipe"]["label"],
            "image":recipeJson["recipe"]["image"],
            "yield":recipeJson["recipe"]["yield"],
            "ingredients":recipeJson["recipe"]["ingredientLines"],
            "instruction":recipeJson["recipe"]["url"],
        }
        return render(request, "pages/home.html", {'recipe' : output, 'r' : recipe})


@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.userprofile is None:
            user_profile = Profile(user=request.user)
            user_profile.save()
    return render(request, 'users/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.userprofile is None:
            user_profile = Profile(user=request.user)
            user_profile.save()
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your account has been updated!')
            return redirect("profile")
    else:
        Profile.objects.get_or_create(user=request.user)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "pages/myProfile.html", context)


def about_view(response):
    return render(response, "pages/aboutUs.html", {})

def news_view(response):
    return render(response, "pages/soon.html", {})

def contact_view(response):
    return render(response, "pages/contactUs.html", {})

def help_view(response):
    return render(response, "pages/soon.html", {})

def redirect_login(response):
    response = redirect('login/')
    return response

def redirect_logout(response):   
    response = redirect('logout/')
    return response

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "pages/edit_settings.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user