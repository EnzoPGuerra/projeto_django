from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from recipes.tests.test_recipe_base import RecipeMixin
from unittest.mock import patch

class RecipeBaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
    def sleep(self, seconds=5):
        time.sleep(seconds)

    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()
    
    def tearDown(self) -> None:
        self.browser.quit()      
        return super().tearDown()

class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest):
    
    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_homepage_without_recipe_not_found_message(self):
        self.browser.get(self.live_server_url)   
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found', body.text)

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_search_input_can_find_correct_recipes(self):
        title_needed = 'This is what I need'
        recipes = self.make_recipe_alot()
        recipes[0].title = title_needed
        recipes[0].save()
        self.browser.get(self.live_server_url)
        search_input = self.browser.find_element(By.XPATH, '//input[@placeholder="Search for a Recipe"]')
        search_input.send_keys(recipes[0].title)
        search_input.send_keys(Keys.ENTER)

        self.assertIn(title_needed, self.browser.find_element(By.TAG_NAME, 'body').text)

        self.sleep(6)

    @patch('recipes.views.PER_PAGE', new=2)
    def test_recipe_homepage_without_recipe_not_found_message(self):

        self.make_recipe_alot() 
        #Usuário abre a página
        self.browser.get(self.live_server_url)   
        next_page = self.browser.find_element(By.XPATH, '//a[@aria-label="Go to page 2"]')
        next_page.click()

        self.assertEqual(
            len(self.browser.find_elements(By.CLASS_NAME, 'recipe-list-item')),
            2)