from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    start_bid = models.FloatField()
    image_url = models.URLField(max_length=300)
    category = models.CharField(max_length=32)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | start price: ${round(self.start_bid, 2)}"