from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import PasswordChangingForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            login(response, user)
            return redirect('/home')
    form = RegisterForm()
    return render(response, "register/register.html", {"form":form})


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("edit_settings")