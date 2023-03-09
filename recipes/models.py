from django.db import models
from django.contrib.auth.models import User
from random import randint

# Create your models here.
#

def rand_ratio():
    return randint(840, 900), randint(473, 573)

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='https://loremflickr.com/%s/%s/food,cook' % rand_ratio())
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title





