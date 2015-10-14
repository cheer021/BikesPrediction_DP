from django.db import models

class Station(models.Model):
	station_id = models.IntegerField(primary_key = True, default = -1)
	name = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=15, decimal_places=12)
	longitude = models.DecimalField(max_digits=15, decimal_places=12)

class StationDataNow(models.Model):
    station = models.ForeignKey('Station', primary_key = True, default = -1)
    #station_id = models.IntegerField(primary_key = True, default = -1)
    datetime = models.DateTimeField('time now')
    last_comm_with_server = models.DateTimeField('last communication with server')
    nb_bikes = models.IntegerField()
    nb_empty_docks = models.IntegerField()
