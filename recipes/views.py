from django.shortcuts import render, get_object_or_404, get_list_or_404
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
        
    recipes = get_list_or_404( 
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True))

    title = recipes[0].category.name
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': title,
    })


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe.objects.filter(id=id)
    )

    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'is_html': True if recipe.preparation_steps_is_html else False
    })