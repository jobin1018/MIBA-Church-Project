from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages


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


def gallery(request):
    albums = Album.objects.all()

    context = {"albums": albums}
    return render(request, "mibaapp/gallery.html", context)


def galleryDetail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    albumImages = AlbumImages.objects.filter(album=album)

    context = {"album": album, "albumImages": albumImages}
    return render(request, "mibaapp/gallery_details.html", context)


def contact(request):
    name = ""
    email = ""
    message = ""

    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

            subject = "A message from a visitor"

            message = (
                name
                + " with the email "
                + email
                + ", sent the following message:\n\n"
                + message
            )

            send_mail(subject, message, email, ["mibassembly20@gmail.com"])
            messages.success(request, "Your message has been sent")

            return HttpResponseRedirect(request.path_info)

    context = {"form": form}
    return render(request, "mibaapp/contact.html", context)

