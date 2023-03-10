from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from recipes.models import Recipe
from random import randint

numList1=[]
numList2=[]

for i in range(1, 50):
    numList1.append(randint(840, 900))
    numList2.append(randint(473, 573))

num1 = int(randint(840, 900))
num2 = int(randint(473, 573))
cover = f'https://loremflickr.com/{num1}/{num2}/food,cook'
...

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id') # noqa: E501,E26z
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'numList1': numList1,
        'numList2': numList2
        #'cover_fake': cover
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


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for {search_term}',
        'search_term': search_term

    })

