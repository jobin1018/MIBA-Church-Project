from django.db import models


class Sermons(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sermons"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class PrayerRequests(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=500, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "PrayerRequests"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title


class Hub(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    hub_image = models.ImageField(default="hub_default.jpg", upload_to="hub_images")
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Hub"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title
