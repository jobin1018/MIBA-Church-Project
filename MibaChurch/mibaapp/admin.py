from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sermons)
admin.site.register(PrayerRequests)
admin.site.register(Hub)


# Custom titles
admin.site.site_header = "MIBA Admin"
admin.site.index_title = "MIBA Admin Panel"
admin.site.site_title = "MIBA Australia"
