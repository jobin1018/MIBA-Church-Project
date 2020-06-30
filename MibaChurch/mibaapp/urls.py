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
    path("contact/", views.contact, name="contact"),
    path("hub/<int:pk>/", views.hubDetail, name="hub_detail"),
]
