from django.urls import path
from . import views

urlpatterns = [
    path("", views.search, name="home"),
    path("search/", views.search, name="search"),
    path("book/<slug:slug>/", views.book_detail, name="book_detail"),
]