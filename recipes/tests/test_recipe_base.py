
from django.test import TestCase
from random import randint
from django.contrib.auth.models import User
from recipes import models

def rand_ratio():
    return randint(840, 900), randint(473, 573)


class RecipeMixin:
    
    def make_category(self, name='Category'):
        return models.Category.objects.create(name=name)
    
    def make_author(
            self,
            first_name='Usu',
            last_name='ário',
            username='usuário',
            password='123',
            email='123user@gmail.com'):
        return User.objects.create(
                first_name=first_name, 
                last_name=last_name, 
                username=username, 
                password=password, 
                email=email)

    def make_recipe(
            self,
            title='Receita Teste',
            description='Descrição teste',
            preparation_time=25, 
            slug='test-slug',
            preparation_time_unit='min',
            servings=5,
            servings_unit='pessoas',
            preparation_steps='preparation steps test',
            preparation_steps_is_html=False,
            is_published=True,
            cover='https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
            category=None,
            author=None):
        
        if category is None:
            category={}
        
        if author is None:
            author={}

        return models.Recipe.objects.create(
                title=title,
                description=description,
                preparation_time=preparation_time, 
                slug=slug,
                preparation_time_unit=preparation_time_unit,
                servings=servings,
                servings_unit=servings_unit,
                preparation_steps=preparation_steps,
                preparation_steps_is_html=preparation_steps_is_html,
                is_published=is_published,
                cover=cover,
                category=self.make_category(**category),
                author=self.make_author(**author))
    
    def make_recipe_alot(self, qtd=10):
        recipes = []
        for i in range(qtd):
            kwargs = {
                'title': f'Recipe Title {i}',
                'slug': f'r{i}', 
                'author': {'username': f'u{i}'}}
            recipe = self.make_recipe(**kwargs)
            recipes.append(recipe)
        return recipes


class RecipesTestBase(TestCase, RecipeMixin):
    def setUp(self) -> None:
        return super().setUp()
