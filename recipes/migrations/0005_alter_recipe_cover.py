# Generated by Django 4.1.7 on 2023-03-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default=None, upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]