# Generated by Django 4.0.3 on 2022-03-20 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='end_date_exp',
            new_name='end_date_expected',
        ),
    ]
