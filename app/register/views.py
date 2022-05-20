from django.shortcuts import  get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from .forms import RegisterForm, EditProfileForm,PasswordChangingForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/recipes")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("edit_profile")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

class ShowProfilePageView(DetailView):
    model = Profile
    template_name ="registration/user_profile.html"

    def get_context_data(self,*args, **kwargs):
      
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name ="registration/edit_profile_page.html"
    success_url = reverse_lazy("home")
    fields = ["bio","profile_image"]


