from django import forms
from .models import Photo

class RecipePhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']