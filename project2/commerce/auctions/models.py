from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User




class User(AbstractUser):
    pass

class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Bid(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    bid = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.author}: ${self.bid}"

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writter")
    comment = models.TextField(max_length=256)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} at {self.creation}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    start_bid = models.DecimalField(max_digits=100, decimal_places=2)
    image_url = models.URLField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="type", blank=True, null=True, default="No Category")
    creation = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auctioneer")
    bid = models.ForeignKey(Bid, blank=True, null=True, on_delete=models.SET_NULL, related_name="offers")
    comments = models.ManyToManyField(Comments, blank=True, related_name="listing")
    bids_count = models.IntegerField(default=1)
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="favorites")
    activated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} | price: ${self.bid}"