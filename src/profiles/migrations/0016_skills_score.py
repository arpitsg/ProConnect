# Generated by Django 4.0.3 on 2022-03-26 15:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_remove_languages_proficiency_languages_proficiency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
