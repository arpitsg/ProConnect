# Generated by Django 4.0.3 on 2022-03-26 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_skills_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='score',
            new_name='proficiency',
        ),
    ]
