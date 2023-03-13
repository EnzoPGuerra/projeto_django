
from django.urls import reverse, resolve
from .test_recipe_base import RecipesTestBase
from recipes import views, models

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