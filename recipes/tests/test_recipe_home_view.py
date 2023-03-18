
from django.urls import reverse, resolve
from .test_recipe_base import RecipesTestBase
from recipes import views, models
from unittest.mock import patch

class RecipeHomeViewsTest(RecipesTestBase):
   
    #Home
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_home_view_return_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_return_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))
    
    def test_if_home_template_loads_recipes(self):
        self.make_recipe()       
        response = self.client.get(reverse('recipes:home'))
        response_content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        #Uso o decode para transformar binário em string
        self.assertIn('Receita Teste', response_content)
        self.assertEqual(len(response_context_recipes), 1)
    
    @patch('recipes.views.PER_PAGE', new=6)
    def test_recipe_home_is_paginated(self):
        for i in range(18):
            kwargs = {'author': {'username': f'u{i}'}, 'slug': f's{i}'}
            self.make_recipe(**kwargs)

        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes'] 
        paginator = recipes.paginator

        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 6)
        ...
        