from .test_recipe_base import RecipesTestBase
from django.core.exceptions import ValidationError

class CategoryModelsTest(RecipesTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(name='Testing CategoryModel')
        return super().setUp()
    
    def test_category_name_maxlength(self):
        self.category.name = 'A' * 121

        with self.assertRaises(ValidationError):
            self.category.full_clean()
    
    def test_category_string_representation(self):
        self.category.name = 'Testing Representation'
        self.assertEqual(str(self.category), 'Testing Representation')
