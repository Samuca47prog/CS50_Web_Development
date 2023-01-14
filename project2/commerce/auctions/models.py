from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="type", blank=True, null=True, default="No Category")
    creation = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctioneer")

    def __str__(self):
        return f"{self.title} | start price: ${self.start_bid}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lover")
    watchlist = models.ManyToManyField(Listing, blank=True, related_name="favorited")
