<<<<<<< HEAD
from django.shortcuts import  render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from .forms import RegisterForm, EditProfileForm,PasswordChangingForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

=======
from django.shortcuts import render, redirect
from .forms import RegisterForm
>>>>>>> parent of 2741b71 (resoved conflicts)

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = RegisterForm()
<<<<<<< HEAD
    return render(response, "register/register.html", {"form":form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

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

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("edit_profile")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name ="registration/edit_profile_page.html"
    success_url = reverse_lazy("home")
    fields = ["bio","profile_image"]


=======
    return render(response, "register/register.html", {"form":form})
>>>>>>> parent of 2741b71 (resoved conflicts)
