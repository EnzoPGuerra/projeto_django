from django.http import Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from recipes.models import Recipe
from random import randint
from django.db.models import Q
from utils.pagination import make_pagination
from django.contrib import messages

import os

PER_PAGE = int(os.environ.get('PER_PAGE',6))

numList1=[]
numList2=[]

for i in range(1, 50):
    numList1.append(randint(840, 900))
    numList2.append(randint(473, 573))

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id') # noqa: E501,E26z
    
    page_obj, pagination_range = make_pagination(request, querySet=recipes, per_page=PER_PAGE)

    messages.success(request, 'BOAAAAA 06! Fatio... Passou!')
 
    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'numList1': numList1,
        'numList2': numList2
    })


def category(request, category_id):
        
    recipes = get_list_or_404( 
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True))

    title = recipes[0].category.name
    
    page_obj, pagination_range = make_pagination(request, querySet=recipes, per_page=PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': title,
        'numList1': numList1,
        'numList2': numList2
    })


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe.objects.filter(id=id)
    )

    return render(request, 'recipes/pages/recipe_view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'is_html': True if recipe.preparation_steps_is_html else False,
        'numList1': numList1,
        'numList2': numList2

    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(description__icontains=search_term)),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, querySet=recipes, per_page=PER_PAGE)

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for {search_term}',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'numList1': numList1,
        'numList2': numList2,
        'additional_url_query': f'&q={search_term}'
    })
