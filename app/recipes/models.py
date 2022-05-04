from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_url = models.CharField(max_length=500)
    image_url = models.CharField(max_length=500)
    ingredient = models.CharField(max_length=500)
    calories = models.CharField(max_length=50)
    total_time = models.CharField(max_length=10)
    cuisine = models.CharField(max_length=100)
    mealType = models.CharField(max_length=100)
    dishType = models.CharField(max_length=100)
