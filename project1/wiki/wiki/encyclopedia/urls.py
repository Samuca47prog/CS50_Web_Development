from unicodedata import name
from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("createNewPage", views.createNewPage, name="createNewPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("page/<str:name>", views.renderPage, name="renderPage")
]
