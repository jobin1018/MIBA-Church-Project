from django.contrib import admin
from .models import *

# Register your models here.
class SermonsAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")


admin.site.register(Sermons, SermonsAdmin)


class SongsAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")


admin.site.register(Songs, SongsAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")


admin.site.register(Article, ArticleAdmin)


class KidsAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")


admin.site.register(KidsCorner, KidsAdmin)


class AlbumImagesAdmin(admin.StackedInline):
    model = AlbumImages


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "date_posted")

    inlines = [AlbumImagesAdmin]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Album


@admin.register(AlbumImages)
class AlbumImagesAdmin(admin.ModelAdmin):
    pass


# Custom titles
admin.site.site_header = "MIBA Admin"
admin.site.index_title = "MIBA Admin Panel"
admin.site.site_title = "MIBA Australia"
