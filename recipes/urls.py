# recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('new/', views.create_recipe, name='create_recipe'),
    path('view/<int:recipe_id>/', views.view_recipe, name='view_recipe'),
]