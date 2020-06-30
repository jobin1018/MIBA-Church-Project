from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


def home(request):
    context = {}
    return render(request, "mibaapp/home.html", context)


def about(request):
    context = {}
    return render(request, "mibaapp/about.html", context)


def sermons(request):
    sermonsObj = Sermons.objects.all()

    for sermon in sermonsObj:
        sermon.link = sermon.link.split("/")[-1]

    context = {"sermons": sermonsObj}
    return render(request, "mibaapp/sermons.html", context)


def prayerRequests(request):
    prayerReqs = PrayerRequests.objects.all()

    context = {"prayerReqs": prayerReqs}
    return render(request, "mibaapp/prayer_requests.html", context)


def hub(request):
    hubItems = Hub.objects.all()

    context = {"hubItems": hubItems}
    return render(request, "mibaapp/hub.html", context)


def hubDetail(request, pk):
    hubItem = get_object_or_404(Hub, pk=pk)

    context = {"hubItem": hubItem}
    return render(request, "mibaapp/hub_details.html", context)


def contact(request):
    context = {}
    return render(request, "mibaapp/contact.html", context)

