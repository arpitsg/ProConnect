# Generated by Django 3.2 on 2022-04-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20220415_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='is_current',
            field=models.BooleanField(default=True),
        ),
    ]
