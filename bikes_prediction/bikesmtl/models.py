from django.db import models
from django.utils import timezone
import datetime

class Station(models.Model):
    station_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=15, decimal_places=12)
    longitude = models.DecimalField(max_digits=15, decimal_places=12)
    updated_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['station_id', 'name', 'latitude', 'longitude']

class StationDataNow(models.Model):
    station = models.ForeignKey(Station, primary_key = True)
    updated_at = models.DateTimeField(auto_now=True)
    last_comm_with_server = models.DateTimeField('last communication with server')
    nb_bikes = models.IntegerField()
    nb_empty_docks = models.IntegerField()

    REQUIRED_FIELDS = ['station', 'last_comm_with_server', 'nb_bikes', 'nb_empty_docks']
