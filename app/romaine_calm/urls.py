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
from pages.views import profile_view
from pages.views import news_view
from pages.views import contact_view
from pages.views import add_recipe_view
from pages.views import favorite_view
from register import views as v
from recipes.views import index_view
from recipes.views import all_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name= 'home'),
    path('help/', help_view, name ='help'),
    path('register/', v.register, name="register"),
    path('recipes/', all_view, name= "recipes"),
    path('recipes/<id>', index_view),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name= 'profile'),
    path('about/', about_view, name= 'about'),
    path('news/', news_view, name= 'news'),
    path('contact/', contact_view, name= 'contact'),
    path('add_recipe/', add_recipe_view, name= 'add_recipe'),
    path('favorite/', favorite_view, name= 'favorite')

]
