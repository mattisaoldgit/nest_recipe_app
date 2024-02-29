# recipes/models.py

from django.db import models
from django.contrib.auth.models import User
from food_items.models import FoodItem


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    food_items = models.ManyToManyField(FoodItem)

    def __str__(self):
        return self.title