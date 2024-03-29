# Generated by Django 3.2 on 2022-04-12 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company_profile', '0006_job_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='url',
        ),
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company', models.BooleanField(default=True)),
                ('r', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
