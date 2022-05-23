from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
# Create your views here.

# HOMEPAGE
def homepage_view(response):
    #return HttpResponse("<h1>HomePage</h1>")
    return render(response, "pages/home.html", {})

@login_required
def profile(request):
    if request.method == 'POST':
            u_form = UserUpdateForm(request.POST,instance=request.user)
            p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f' Your account has been updated!')
                return redirect("profile")
    else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, "pages/myProfile.html", context)


def favorite_view(response):
    return render(response, "pages/favorite.html", {})

def about_view(response):
    return render(response, "pages/aboutUs.html", {})

def news_view(response):
    return render(response, "pages/soon.html", {})

def contact_view(response):
    return render(response, "pages/contactUs.html", {})

def add_recipe_view(response):
    return render(response, "pages/addUserRecipe.html", {})

#TEST CAN BE REMOVED FOR PRODUCTION

def help_view(response):
    return render(response, "pages/soon.html", {})