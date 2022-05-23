#from asyncio.windows_events import NULL
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_id = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingredients(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    ingredient_quantity =  models.CharField(max_length=100)