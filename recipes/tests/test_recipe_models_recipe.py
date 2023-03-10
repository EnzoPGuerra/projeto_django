from .test_recipe_base import RecipesTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes import models
from random import randint

def rand_ratio():
    return randint(840, 900), randint(473, 573)

class RecipeModelsTest(RecipesTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    #nesse caso meu teste vai falhar se o for colocado o tamanho correto 

    def make_recipe_defaults(self):
        recipe = models.Recipe(
            title='Receita Teste',
            description='Descrição teste',
            preparation_time=25, 
            slug='test_slug',
            preparation_time_unit='min',
            servings=5,
            servings_unit='pessoas',
            preparation_steps='preparation steps test',
            cover='https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
            category=self.make_category(name='Teste Default'),
            author=self.make_author(username='newuser')
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
            ('title', 120),
            ('description', 120),
            ('servings_unit', 65),
            ('preparation_time_unit', 65)
        ])
    
    def test_recipe_fields_max_lenth(self, field, max_length):
        setattr(self.recipe, field, 'a' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_default(self):
        recipe = self.make_recipe_defaults()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_preparation_steps_is_published_default(self):
        recipe = self.make_recipe_defaults()
        self.assertFalse(recipe.is_published)

    def test_recipe_string_representation(self):
        self.recipe.title = 'Testing Representation'
        self.assertEqual(str(self.recipe), 'Testing Representation')