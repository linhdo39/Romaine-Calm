from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
