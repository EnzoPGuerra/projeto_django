
from django.urls import reverse, resolve
from .test_recipe_base import RecipesTestBase
from recipes import views, models

class RecipeCategoryViewsTest(RecipesTestBase):

    #Category
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertIs(view.func, views.category)
    
    def test_category_view_return_404_if_no_categorys_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)


