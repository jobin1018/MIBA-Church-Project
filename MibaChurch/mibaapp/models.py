from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse


class Sermons(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    sermon_image = ResizedImageField(
        size=[1000, 550],
        quality=100,
        blank=True,
        default="sermon_default.jpg",
        upload_to="sermon_images",
    )
    link = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sermons"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Songs(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    song_image = ResizedImageField(
        size=[1000, 550],
        quality=100,
        blank=True,
        default="songs_default.jpg",
        upload_to="songs_images",
    )
    link = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Songs"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    pdf = models.FileField(upload_to="article_pdfs", blank=True, null=True)
    article_image = ResizedImageField(
        size=[1000, 550],
        quality=100,
        blank=True,
        default="article_default.jpg",
        upload_to="article_images",
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Articles"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class KidsCorner(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    kids_image = ResizedImageField(
        size=[1000, 550],
        quality=100,
        blank=True,
        default="hub_default.jpg",
        upload_to="hub_images",
    )
    link = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "KidsCorner"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = "Album"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery_detail", kwargs={"slug": self.slug})


class AlbumImages(models.Model):
    album = models.ForeignKey(Album, default=None, on_delete=models.CASCADE)
    image = ResizedImageField(size=[1000, 550], quality=100, upload_to="gallery_images")
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "AlbumImages"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.album.title

