# Generated by Django 3.2 on 2022-04-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0016_application_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Active', 'ACTIVE'), ('Selected', 'SELECTED'), ('Rejected', 'REJECTED'), {'INTERVIEW', 'Interview'}], default='A', max_length=15),
        ),
    ]
