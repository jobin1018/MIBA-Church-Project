from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("sermons/", views.sermons, name="sermons"),
    path("prayerRequests/", views.prayerRequests, name="prayer_requests"),
    path("hub/", views.hub, name="hub"),
    path("hub/search/", views.hubSearch, name="hub_search"),
    path("contact/", views.contact, name="contact"),
    path("hub/<slug:slug>/", views.hubDetail, name="hub_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<slug:slug>/", views.galleryDetail, name="gallery_detail"),
    path("sermons/search/", views.sermonsSearch, name="sermons_search"),
]
