# Generated by Django 4.1 on 2023-01-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0009_listing_watchlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="activated",
            field=models.BooleanField(default=True),
        ),
    ]
