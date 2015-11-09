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

class StationDataPredictions(models.Model):
    station = models.ForeignKey(Station, primary_key = True)
    updated_at = models.DateTimeField(auto_now=True)
    nb_bikes_5 = models.IntegerField()
    nb_empty_docks_5 = models.IntegerField()
    nb_bikes_10 = models.IntegerField()
    nb_empty_docks_10 = models.IntegerField()
    nb_bikes_15 = models.IntegerField()
    nb_empty_docks_15 = models.IntegerField()
    nb_bikes_30 = models.IntegerField()
    nb_empty_docks_30 = models.IntegerField()

    REQUIRED_FIELDS = ['station', 'updated_at', 'nb_bikes_5', 'nb_empty_docks_5', 'nb_bikes_10', 'nb_empty_docks_10', 'nb_bikes_15', 'nb_empty_docks_15', 'nb_bikes_30', 'nb_empty_docks_30']
