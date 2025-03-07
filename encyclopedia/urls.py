from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random", views.random_entry, name="random"),
    path("new", views.new_entry, name="new"),
    path("edit", views.edit, name="edit"),
    path("search", views.search, name="search")
]
