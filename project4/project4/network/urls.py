
from django.urls import path

from . import views

urlpatterns = [
    # Login
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Posts
    path("add_post", views.add_post, name="add_post"),
]
