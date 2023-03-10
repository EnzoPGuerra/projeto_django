
from django.urls import reverse, resolve
from .test_recipe_base import RecipesTestBase
from recipes import views, models

class RecipeSearchViewsTest(RecipesTestBase):
   
    #Search
    def test_recipe_search_view_function_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_search_view_return_correct_template(self):
        response = self.client.get(reverse('recipes:search')+'?q=k')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search')+'?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &lt;Teste&gt;',
            response.content.decode('utf-8'))
        ...