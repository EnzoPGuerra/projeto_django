from django.contrib import admin
from . import models

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    ...

class recipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(models.Category, categoryAdmin)
admin.site.register(models.Recipe, recipeAdmin)
