# Generated by Django 4.1.7 on 2023-02-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_category_alter_recipe_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/cover/%y/%m/%d/'),
        ),
    ]
