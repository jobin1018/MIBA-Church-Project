from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


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

    paginator = Paginator(sermonsObj, 12)
    page = request.GET.get("page")
    sermonsObj = paginator.get_page(page)

    context = {"sermons": sermonsObj}
    return render(request, "mibaapp/sermons.html", context)


def sermonsSearch(request):
    query = request.GET.get("q", "")
    if query:
        queryset = Q(title__icontains=query)
        sermonsSearchResult = Sermons.objects.filter(queryset).distinct()
        for sermon in sermonsSearchResult:
            sermon.link = sermon.link.split("/")[-1]
    else:
        sermonsSearchResult = []

    context = {"sermonsSearchResult": sermonsSearchResult, "query": query}
    return render(request, "mibaapp/sermons_search.html", context)


def prayerRequests(request):
    prayerReqs = PrayerRequests.objects.all()

    paginator = Paginator(prayerReqs, 10)
    page = request.GET.get("page")
    prayerReqs = paginator.get_page(page)

    context = {"prayerReqs": prayerReqs}
    return render(request, "mibaapp/prayer_requests.html", context)


def hub(request):
    hubItems = Hub.objects.all()

    paginator = Paginator(hubItems, 12)
    page = request.GET.get("page")
    hubItems = paginator.get_page(page)

    context = {"hubItems": hubItems}
    return render(request, "mibaapp/hub.html", context)


def hubDetail(request, slug):
    hubItem = get_object_or_404(Hub, slug=slug)

    context = {"hubItem": hubItem}
    return render(request, "mibaapp/hub_details.html", context)


def hubSearch(request):
    query = request.GET.get("r", "")
    print(query)
    if query:
        queryset = Q(title__icontains=query) | Q(content__icontains=query)
        hubSearchResult = Hub.objects.filter(queryset).distinct()
        print(hubSearchResult)
    else:
        hubSearchResult = []

    context = {"hubSearchResult": hubSearchResult, "query": query}
    return render(request, "mibaapp/hub_search.html", context)


def gallery(request):
    albums = Album.objects.all()

    paginator = Paginator(albums, 12)
    page = request.GET.get("page")
    albums = paginator.get_page(page)

    context = {"albums": albums}
    return render(request, "mibaapp/gallery.html", context)


def galleryDetail(request, slug):
    album = get_object_or_404(Album, slug=slug)
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

            send_mail(subject, message, email, ["mbassembly@yahoo.com"])
            messages.success(request, "Your message has been sent")

            return HttpResponseRedirect(request.path_info)

    context = {"form": form}
    return render(request, "mibaapp/contact.html", context)

