# recipes/forms.py

from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'food_items', 'ingredients', 'instructions']
        widgets = {
            'food_items': forms.SelectMultiple()
        }        