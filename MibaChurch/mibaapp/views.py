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


def songs(request):
    songsObj = Songs.objects.all()

    for song in songsObj:
        song.link = song.link.split("/")[-1]

    paginator = Paginator(songsObj, 12)
    page = request.GET.get("page")
    songsObj = paginator.get_page(page)

    context = {"songs": songsObj}
    return render(request, "mibaapp/songs.html", context)


def songsSearch(request):
    query = request.GET.get("q", "")
    if query:
        queryset = Q(title__icontains=query)
        songsSearchResult = Songs.objects.filter(queryset).distinct()
        for song in songsSearchResult:
            song.link = song.link.split("/")[-1]
    else:
        songsSearchResult = []

    context = {"songsSearchResult": songsSearchResult, "query": query}
    return render(request, "mibaapp/songs_search.html", context)


def article(request):
    articles = Article.objects.all()

    paginator = Paginator(articles, 10)
    page = request.GET.get("page")
    articles = paginator.get_page(page)

    context = {"articles": articles}
    return render(request, "mibaapp/articles.html", context)


def articleSearch(request):
    query = request.GET.get("q", "")
    if query:
        queryset = Q(title__icontains=query)
        articleSearchResult = Article.objects.filter(queryset).distinct()
    else:
        articleSearchResult = []

    context = {"articleSearchResult": articleSearchResult, "query": query}
    return render(request, "mibaapp/articles_search.html", context)


def kidsCorner(request):
    kidsItems = KidsCorner.objects.all()

    for item in kidsItems:
        item.link = item.link.split("/")[-1]

    paginator = Paginator(kidsItems, 12)
    page = request.GET.get("page")
    kidsItems = paginator.get_page(page)

    context = {"kidsItems": kidsItems}
    return render(request, "mibaapp/kids.html", context)


def kidsSearch(request):
    query = request.GET.get("r", "")

    if query:
        queryset = Q(title__icontains=query)
        kidsSearchResult = KidsCorner.objects.filter(queryset).distinct()
        for item in kidsSearchResult:
            item.link = item.link.split("/")[-1]
    else:
        kidsSearchResult = []

    context = {"kidsSearchResult": kidsSearchResult, "query": query}
    return render(request, "mibaapp/kids_search.html", context)


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

