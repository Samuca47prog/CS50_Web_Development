from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    following = models.ManyToManyField(User, blank=True, related_name="followers")
    followers = models.ManyToManyField(User, blank=True, related_name="following")

    def __str__(self):
        return self.user.username

class Posts(models.Model):
    posted_date = models.DateTimeField("Posted date", auto_now_add=True)
    last_update = models.DateTimeField("Last update", auto_now=True)
    content = models.TextField("Post content")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + " at " + self.posted_date.strftime("%m/%d/%Y, %H:%M:%S")