
from django.urls import reverse, resolve
from .test_recipe_base import RecipesTestBase
from recipes import views, models

class RecipeRecipeViewsTest(RecipesTestBase):    

    #Recipe
    def test_recipe_recipe_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
    
    def test_recipe_view_return_404_if_no_recipe_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)