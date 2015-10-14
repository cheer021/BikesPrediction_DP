from django.contrib import admin

from .models import Station, StationDataNow

admin.site.register(Station)
admin.site.register(StationDataNow)