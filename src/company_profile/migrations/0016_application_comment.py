# Generated by Django 3.2 on 2022-04-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0015_alter_company_profile_about_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='comment',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
