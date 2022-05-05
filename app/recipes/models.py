from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_id = models.CharField(max_length=500)
    
