from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sermons/", views.sermons, name="sermons"),
    path("songs/", views.songs, name="songs"),
    path("articles/", views.article, name="articles"),
    path("articles/search/", views.articleSearch, name="articles_search"),
    path("kids_corner/", views.kidsCorner, name="kids_corner"),
    path("kids_corner/search/", views.kidsSearch, name="kids_search"),
    path("contact/", views.contact, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<slug:slug>/", views.galleryDetail, name="gallery_detail"),
    path("sermons/search/", views.sermonsSearch, name="sermons_search"),
    path("songs/search/", views.songsSearch, name="songs_search"),
]
