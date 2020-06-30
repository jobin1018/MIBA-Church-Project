from django.db import models


class Sermons(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sermons"

    def __str__(self):
        return self.title

