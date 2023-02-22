from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe(request, id):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': recipes,
        'is_detail_page': True
    })