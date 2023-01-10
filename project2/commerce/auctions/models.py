from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=128)
    start_bid = models.FloatField()
    image_url = models.URLField(max_length=200)
    category = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.title} | init price: ${round(self.start_bid, 2)}"