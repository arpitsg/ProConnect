# Generated by Django 3.2 on 2022-04-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0012_savedjob_saved_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]