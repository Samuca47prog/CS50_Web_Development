
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
    path("all_posts", views.all_posts, name="all_posts"),
    path("edit_post/<post_id>", views.edit_post, name="edit_post"),
    path("like_deslike_post/<post_id>", views.like_deslike_post, name="like_deslike_post"),

    # Profile page
    path("user_profile/<user_id>", views.user_profile, name="user_profile"),
    path("add_follower/<user_id>", views.add_follower, name="add_follower"),
    path("remove_follower/<user_id>", views.remove_follower, name="remove_follower"),

    # Following
    path("followings", views.followings, name="followings"),
]
