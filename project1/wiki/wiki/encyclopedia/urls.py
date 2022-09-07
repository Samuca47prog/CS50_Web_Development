from unicodedata import name
from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("createNewPage", views.createNewPage, name="createNewPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("editPage/<str:name>", views.editPage, name="editPage"),
    path("page/<str:name>", views.renderPage, name="renderPage")
]
