#from asyncio.windows_events import NULL
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_id = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    userRecipe = models.BooleanField()
    def __str__(self):
        return self.name


class UserRecipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    recipe_photo = models.ImageField(upload_to='images/', null=True, verbose_name="")
    ingredient = models.CharField(max_length=5000)
    total_hours = models.CharField(max_length=100)
    total_mins = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)
    preparation = models.CharField(max_length=10000)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.CharField(max_length=100)

class Ingredients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    ingredient_quantity =  models.CharField(max_length=100)
    expiration_date = models.DateField()

