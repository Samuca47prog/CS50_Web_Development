from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    path("delete-auction/<int:listing_id>", views.delete_auction, name="delete-auction"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_bid/<int:listing_id>", views.add_bid, name="add_bid")
]
