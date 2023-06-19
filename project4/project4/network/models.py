from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Posts(models.Model):
    posted_date = models.DateTimeField("Posted date", auto_now_add=True)
    last_update = models.DateTimeField("Last update", auto_now=True)
    content = models.TextField("Post content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " at " + self.posted_date.strftime("%m/%d/%Y, %H:%M:%S")