# Generated by Django 3.2 on 2022-04-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0013_alter_job_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]
