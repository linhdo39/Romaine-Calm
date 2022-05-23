"""romaine_calm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.urls import include
from django.contrib import admin
from django.urls import path
from pages.views import about_view
from pages.views import homepage_view
from pages.views import help_view
from pages import views as user_views
from pages.views import news_view
from pages.views import contact_view
from pages.views import add_recipe_view
from pages.views import favorite_view
from pages.views import redirect_login
from pages.views import redirect_logout
from pages.views import redirect_register
from register import views as v
from recipes.views import index_view
from recipes.views import all_view
from django.conf import settings
from django.conf.urls.static import static
from pages.views import UserEditView
from register.views import PasswordChangeView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', homepage_view, name= 'home'),
    path('home/', homepage_view, name= 'home'),
    path('help/', help_view, name ='help'),
    path('register/', v.register, name="register"),
    path('recipes/', all_view, name= "recipes"),
    path('recipes/<id>', index_view),
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_views.profile, name= 'profile'),
     path('edit_settings', UserEditView.as_view(), name='edit_settings'),
    path('password/',  PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('about/', about_view, name= 'about'),
    path('news/', news_view, name= 'news'),
    path('contact/', contact_view, name= 'contact'),
    path('add_recipe/', add_recipe_view, name= 'add_recipe'),
    path('favorite/', favorite_view, name= 'favorite'),
    path('login', redirect_login),
    path('logout', redirect_logout),
    path('register', redirect_register)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
