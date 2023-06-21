# Generated by Django 4.1 on 2023-06-21 12:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="posts",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]