# Generated by Django 4.2.9 on 2024-02-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0001_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='food_items',
            field=models.ManyToManyField(to='food_items.fooditem'),
        ),
    ]
