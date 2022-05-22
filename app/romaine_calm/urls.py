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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from pages.views import profile_view
>>>>>>> 3909872 (adding new code)
from pages.views import help_view
from pages.views import profile_view
=======
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
from pages.views import profile_view
from pages.views import help_view
from register import views as v
from recipes.views import index_view
from recipes.views import all_view
from register.views import UserEditView, PasswordChangeView,EditProfilePageView
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
from pages.views import news_view
from pages.views import contact_view
from pages.views import add_recipe_view
from pages.views import favorite_view
from register import views as v
from recipes.views import index_view
from recipes.views import all_view
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from register import views as user_views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 3909872 (adding new code)
=======
from register import views as user_views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 3909872 (adding new code)
=======
from register import views as user_views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 3909872 (adding new code)
=======
from register import views as user_views
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> 3909872 (adding new code)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name= 'home'),
    path('help/', help_view, name ='help'),
    path('register/', v.register, name="register"),
    path('recipes/', all_view, name= "recipes"),
    path('recipes/<id>', index_view),
    path('', include('django.contrib.auth.urls')),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    path('profile/', profile_view, name= 'profile'),
=======
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
    path('profile/', user_views.profile, name="profile"),
    path('about/', about_view, name='about'),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path('password/',PasswordChangeView.as_view(template_name="registration/change-password.html")),
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
    path('about/', about_view, name= 'about'),
    path('news/', news_view, name= 'news'),
    path('contact/', contact_view, name= 'contact'),
    path('add_recipe/', add_recipe_view, name= 'add_recipe'),
    path('favorite/', favorite_view, name= 'favorite')
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
=======
>>>>>>> 3909872 (adding new code)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
