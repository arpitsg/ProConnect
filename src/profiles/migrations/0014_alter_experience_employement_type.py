# Generated by Django 4.0.3 on 2022-03-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_education_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='employement_type',
            field=models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Self-employed', 'Self-employed'), ('Freelance', 'Freelance'), ('Internship', 'Internship')], max_length=15),
        ),
    ]
