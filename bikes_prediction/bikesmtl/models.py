# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BikesmtlStation(models.Model):
    station = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    latitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    longitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'bikesmtl_station'


# class BikesmtlStationdatanow(models.Model):
#     station_id = models.IntegerField(primary_key=True)
#     updated_at = models.DateTimeField()
#     last_comm_with_server = models.DateTimeField()
#     nb_bikes = models.IntegerField()
#     nb_empty_docks = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'bikesmtl_stationdatanow'


# class BikesmtlStationdatapredictions(models.Model):
#     station_id = models.IntegerField(primary_key=True)
#     updated_at = models.DateTimeField()
#     nb_bikes_5 = models.IntegerField()
#     nb_empty_docks_5 = models.IntegerField()
#     nb_bikes_10 = models.IntegerField()
#     nb_empty_docks_10 = models.IntegerField()
#     nb_bikes_15 = models.IntegerField()
#     nb_empty_docks_15 = models.IntegerField()
#     nb_bikes_30 = models.IntegerField()
#     nb_empty_docks_30 = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'bikesmtl_stationdatapredictions'


# class Data25Ordered(models.Model):
#     station = models.IntegerField(blank=True, null=True)
#     month = models.IntegerField(blank=True, null=True)
#     dayofweek = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     hour = models.IntegerField(blank=True, null=True)
#     minute = models.IntegerField(blank=True, null=True)
#     nbbikes = models.IntegerField(db_column='nbBikes', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks = models.IntegerField(db_column='nbEmptyDocks', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'data_25_ordered'


# class DataFlowHourly(models.Model):
#     station = models.IntegerField(blank=True, null=True)
#     datetime = models.CharField(unique=True, max_length=9, blank=True, null=True)
#     month = models.IntegerField(blank=True, null=True)
#     dayofweek = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     hour = models.IntegerField(blank=True, null=True)
#     bikes_arrived_last_hour = models.IntegerField(blank=True, null=True)
#     bikes_left_last_hour = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'data_flow_hourly'


# class DataHourly(models.Model):
#     station = models.IntegerField(blank=True, null=True)
#     datetime = models.CharField(unique=True, max_length=9, blank=True, null=True)
#     month = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     hour = models.IntegerField(blank=True, null=True)
#     minute = models.IntegerField(blank=True, null=True)
#     nbbikes = models.IntegerField(db_column='nbBikes', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks = models.IntegerField(db_column='nbEmptyDocks', blank=True, null=True)  # Field name made lowercase.
#     id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?

#     class Meta:
#         managed = False
#         db_table = 'data_hourly'


# class DjangoCronCronjoblog(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     code = models.CharField(max_length=64)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     is_success = models.BooleanField()
#     message = models.TextField()
#     ran_at_time = models.TimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'django_cron_cronjoblog'


# class DjangoMigrations(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


class PredictedDataHourly(models.Model):
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    nbbikes4 = models.IntegerField(db_column='nbBikes4', blank=True, null=True)  # Field name made lowercase.
    nbbikes8 = models.IntegerField(db_column='nbBikes8', blank=True, null=True)  # Field name made lowercase.
    nbbikes12 = models.IntegerField(db_column='nbBikes12', blank=True, null=True)  # Field name made lowercase.
    nbbikes16 = models.IntegerField(db_column='nbBikes16', blank=True, null=True)  # Field name made lowercase.
    nbbikes20 = models.IntegerField(db_column='nbBikes20', blank=True, null=True)  # Field name made lowercase.
    nbbikes24 = models.IntegerField(db_column='nbBikes24', blank=True, null=True)  # Field name made lowercase.
    nbbikes28 = models.IntegerField(db_column='nbBikes28', blank=True, null=True)  # Field name made lowercase.
    nbbikes32 = models.IntegerField(db_column='nbBikes32', blank=True, null=True)  # Field name made lowercase.
    nbbikes36 = models.IntegerField(db_column='nbBikes36', blank=True, null=True)  # Field name made lowercase.
    nbbikes40 = models.IntegerField(db_column='nbBikes40', blank=True, null=True)  # Field name made lowercase.
    nbbikes48 = models.IntegerField(db_column='nbBikes48', blank=True, null=True)  # Field name made lowercase.
    nbbikes52 = models.IntegerField(db_column='nbBikes52', blank=True, null=True)  # Field name made lowercase.
    nbbikes56 = models.IntegerField(db_column='nbBikes56', blank=True, null=True)  # Field name made lowercase.
    nbbikes60 = models.IntegerField(db_column='nbBikes60', blank=True, null=True)  # Field name made lowercase.
    nbbikes64 = models.IntegerField(db_column='nbBikes64', blank=True, null=True)  # Field name made lowercase.
    nbbikes68 = models.IntegerField(db_column='nbBikes68', blank=True, null=True)  # Field name made lowercase.
    nbbikes72 = models.IntegerField(db_column='nbBikes72', blank=True, null=True)  # Field name made lowercase.
    nbbikes76 = models.IntegerField(db_column='nbBikes76', blank=True, null=True)  # Field name made lowercase.
    nbbikes80 = models.IntegerField(db_column='nbBikes80', blank=True, null=True)  # Field name made lowercase.
    nbbikes84 = models.IntegerField(db_column='nbBikes84', blank=True, null=True)  # Field name made lowercase.
    nbbikes88 = models.IntegerField(db_column='nbBikes88', blank=True, null=True)  # Field name made lowercase.
    nbbikes92 = models.IntegerField(db_column='nbBikes92', blank=True, null=True)  # Field name made lowercase.
    nbbikes96 = models.IntegerField(db_column='nbBikes96', blank=True, null=True)  # Field name made lowercase.
    nbbikes100 = models.IntegerField(db_column='nbBikes100', blank=True, null=True)  # Field name made lowercase.
    nbbikes104 = models.IntegerField(db_column='nbBikes104', blank=True, null=True)  # Field name made lowercase.
    nbbikes108 = models.IntegerField(db_column='nbBikes108', blank=True, null=True)  # Field name made lowercase.
    nbbikes112 = models.IntegerField(db_column='nbBikes112', blank=True, null=True)  # Field name made lowercase.
    nbbikes116 = models.IntegerField(db_column='nbBikes116', blank=True, null=True)  # Field name made lowercase.
    nbbikes120 = models.IntegerField(db_column='nbBikes120', blank=True, null=True)  # Field name made lowercase.
    nbbikes124 = models.IntegerField(db_column='nbBikes124', blank=True, null=True)  # Field name made lowercase.
    nbbikes128 = models.IntegerField(db_column='nbBikes128', blank=True, null=True)  # Field name made lowercase.
    nbbikes132 = models.IntegerField(db_column='nbBikes132', blank=True, null=True)  # Field name made lowercase.
    nbbikes136 = models.IntegerField(db_column='nbBikes136', blank=True, null=True)  # Field name made lowercase.
    nbbikes140 = models.IntegerField(db_column='nbBikes140', blank=True, null=True)  # Field name made lowercase.
    nbbikes144 = models.IntegerField(db_column='nbBikes144', blank=True, null=True)  # Field name made lowercase.
    nbbikes148 = models.IntegerField(db_column='nbBikes148', blank=True, null=True)  # Field name made lowercase.
    nbbikes152 = models.IntegerField(db_column='nbBikes152', blank=True, null=True)  # Field name made lowercase.
    nbbikes156 = models.IntegerField(db_column='nbBikes156', blank=True, null=True)  # Field name made lowercase.
    nbbikes160 = models.IntegerField(db_column='nbBikes160', blank=True, null=True)  # Field name made lowercase.
    nbbikes164 = models.IntegerField(db_column='nbBikes164', blank=True, null=True)  # Field name made lowercase.
    nbbikes168 = models.IntegerField(db_column='nbBikes168', blank=True, null=True)  # Field name made lowercase.
    nbbikes176 = models.IntegerField(db_column='nbBikes176', blank=True, null=True)  # Field name made lowercase.
    nbbikes180 = models.IntegerField(db_column='nbBikes180', blank=True, null=True)  # Field name made lowercase.
    nbbikes184 = models.IntegerField(db_column='nbBikes184', blank=True, null=True)  # Field name made lowercase.
    nbbikes188 = models.IntegerField(db_column='nbBikes188', blank=True, null=True)  # Field name made lowercase.
    nbbikes192 = models.IntegerField(db_column='nbBikes192', blank=True, null=True)  # Field name made lowercase.
    nbbikes196 = models.IntegerField(db_column='nbBikes196', blank=True, null=True)  # Field name made lowercase.
    nbbikes200 = models.IntegerField(db_column='nbBikes200', blank=True, null=True)  # Field name made lowercase.
    nbbikes204 = models.IntegerField(db_column='nbBikes204', blank=True, null=True)  # Field name made lowercase.
    nbbikes208 = models.IntegerField(db_column='nbBikes208', blank=True, null=True)  # Field name made lowercase.
    nbbikes212 = models.IntegerField(db_column='nbBikes212', blank=True, null=True)  # Field name made lowercase.
    nbbikes216 = models.IntegerField(db_column='nbBikes216', blank=True, null=True)  # Field name made lowercase.
    nbbikes220 = models.IntegerField(db_column='nbBikes220', blank=True, null=True)  # Field name made lowercase.
    nbbikes224 = models.IntegerField(db_column='nbBikes224', blank=True, null=True)  # Field name made lowercase.
    nbbikes228 = models.IntegerField(db_column='nbBikes228', blank=True, null=True)  # Field name made lowercase.
    nbbikes232 = models.IntegerField(db_column='nbBikes232', blank=True, null=True)  # Field name made lowercase.
    nbbikes236 = models.IntegerField(db_column='nbBikes236', blank=True, null=True)  # Field name made lowercase.
    nbbikes244 = models.IntegerField(db_column='nbBikes244', blank=True, null=True)  # Field name made lowercase.
    nbbikes248 = models.IntegerField(db_column='nbBikes248', blank=True, null=True)  # Field name made lowercase.
    nbbikes256 = models.IntegerField(db_column='nbBikes256', blank=True, null=True)  # Field name made lowercase.
    nbbikes260 = models.IntegerField(db_column='nbBikes260', blank=True, null=True)  # Field name made lowercase.
    nbbikes264 = models.IntegerField(db_column='nbBikes264', blank=True, null=True)  # Field name made lowercase.
    nbbikes268 = models.IntegerField(db_column='nbBikes268', blank=True, null=True)  # Field name made lowercase.
    nbbikes272 = models.IntegerField(db_column='nbBikes272', blank=True, null=True)  # Field name made lowercase.
    nbbikes276 = models.IntegerField(db_column='nbBikes276', blank=True, null=True)  # Field name made lowercase.
    nbbikes280 = models.IntegerField(db_column='nbBikes280', blank=True, null=True)  # Field name made lowercase.
    nbbikes284 = models.IntegerField(db_column='nbBikes284', blank=True, null=True)  # Field name made lowercase.
    nbbikes288 = models.IntegerField(db_column='nbBikes288', blank=True, null=True)  # Field name made lowercase.
    nbbikes292 = models.IntegerField(db_column='nbBikes292', blank=True, null=True)  # Field name made lowercase.
    nbbikes304 = models.IntegerField(db_column='nbBikes304', blank=True, null=True)  # Field name made lowercase.
    nbbikes308 = models.IntegerField(db_column='nbBikes308', blank=True, null=True)  # Field name made lowercase.
    nbbikes312 = models.IntegerField(db_column='nbBikes312', blank=True, null=True)  # Field name made lowercase.
    nbbikes316 = models.IntegerField(db_column='nbBikes316', blank=True, null=True)  # Field name made lowercase.
    nbbikes320 = models.IntegerField(db_column='nbBikes320', blank=True, null=True)  # Field name made lowercase.
    nbbikes324 = models.IntegerField(db_column='nbBikes324', blank=True, null=True)  # Field name made lowercase.
    nbbikes328 = models.IntegerField(db_column='nbBikes328', blank=True, null=True)  # Field name made lowercase.
    nbbikes332 = models.IntegerField(db_column='nbBikes332', blank=True, null=True)  # Field name made lowercase.
    nbbikes336 = models.IntegerField(db_column='nbBikes336', blank=True, null=True)  # Field name made lowercase.
    nbbikes340 = models.IntegerField(db_column='nbBikes340', blank=True, null=True)  # Field name made lowercase.
    nbbikes344 = models.IntegerField(db_column='nbBikes344', blank=True, null=True)  # Field name made lowercase.
    nbbikes348 = models.IntegerField(db_column='nbBikes348', blank=True, null=True)  # Field name made lowercase.
    nbbikes356 = models.IntegerField(db_column='nbBikes356', blank=True, null=True)  # Field name made lowercase.
    nbbikes360 = models.IntegerField(db_column='nbBikes360', blank=True, null=True)  # Field name made lowercase.
    nbbikes364 = models.IntegerField(db_column='nbBikes364', blank=True, null=True)  # Field name made lowercase.
    nbbikes368 = models.IntegerField(db_column='nbBikes368', blank=True, null=True)  # Field name made lowercase.
    nbbikes372 = models.IntegerField(db_column='nbBikes372', blank=True, null=True)  # Field name made lowercase.
    nbbikes376 = models.IntegerField(db_column='nbBikes376', blank=True, null=True)  # Field name made lowercase.
    nbbikes380 = models.IntegerField(db_column='nbBikes380', blank=True, null=True)  # Field name made lowercase.
    nbbikes384 = models.IntegerField(db_column='nbBikes384', blank=True, null=True)  # Field name made lowercase.
    nbbikes388 = models.IntegerField(db_column='nbBikes388', blank=True, null=True)  # Field name made lowercase.
    nbbikes392 = models.IntegerField(db_column='nbBikes392', blank=True, null=True)  # Field name made lowercase.
    nbbikes396 = models.IntegerField(db_column='nbBikes396', blank=True, null=True)  # Field name made lowercase.
    nbbikes404 = models.IntegerField(db_column='nbBikes404', blank=True, null=True)  # Field name made lowercase.
    nbbikes408 = models.IntegerField(db_column='nbBikes408', blank=True, null=True)  # Field name made lowercase.
    nbbikes416 = models.IntegerField(db_column='nbBikes416', blank=True, null=True)  # Field name made lowercase.
    nbbikes424 = models.IntegerField(db_column='nbBikes424', blank=True, null=True)  # Field name made lowercase.
    nbbikes428 = models.IntegerField(db_column='nbBikes428', blank=True, null=True)  # Field name made lowercase.
    nbbikes432 = models.IntegerField(db_column='nbBikes432', blank=True, null=True)  # Field name made lowercase.
    nbbikes440 = models.IntegerField(db_column='nbBikes440', blank=True, null=True)  # Field name made lowercase.
    nbbikes444 = models.IntegerField(db_column='nbBikes444', blank=True, null=True)  # Field name made lowercase.
    nbbikes448 = models.IntegerField(db_column='nbBikes448', blank=True, null=True)  # Field name made lowercase.
    nbbikes452 = models.IntegerField(db_column='nbBikes452', blank=True, null=True)  # Field name made lowercase.
    nbbikes456 = models.IntegerField(db_column='nbBikes456', blank=True, null=True)  # Field name made lowercase.
    nbbikes460 = models.IntegerField(db_column='nbBikes460', blank=True, null=True)  # Field name made lowercase.
    nbbikes464 = models.IntegerField(db_column='nbBikes464', blank=True, null=True)  # Field name made lowercase.
    nbbikes468 = models.IntegerField(db_column='nbBikes468', blank=True, null=True)  # Field name made lowercase.
    nbbikes472 = models.IntegerField(db_column='nbBikes472', blank=True, null=True)  # Field name made lowercase.
    nbbikes476 = models.IntegerField(db_column='nbBikes476', blank=True, null=True)  # Field name made lowercase.
    nbbikes480 = models.IntegerField(db_column='nbBikes480', blank=True, null=True)  # Field name made lowercase.
    nbbikes484 = models.IntegerField(db_column='nbBikes484', blank=True, null=True)  # Field name made lowercase.
    nbbikes492 = models.IntegerField(db_column='nbBikes492', blank=True, null=True)  # Field name made lowercase.
    nbbikes496 = models.IntegerField(db_column='nbBikes496', blank=True, null=True)  # Field name made lowercase.
    nbbikes500 = models.IntegerField(db_column='nbBikes500', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks4 = models.IntegerField(db_column='nbEmptyDocks4', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks8 = models.IntegerField(db_column='nbEmptyDocks8', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks12 = models.IntegerField(db_column='nbEmptyDocks12', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks16 = models.IntegerField(db_column='nbEmptyDocks16', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks20 = models.IntegerField(db_column='nbEmptyDocks20', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks24 = models.IntegerField(db_column='nbEmptyDocks24', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks28 = models.IntegerField(db_column='nbEmptyDocks28', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks32 = models.IntegerField(db_column='nbEmptyDocks32', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks36 = models.IntegerField(db_column='nbEmptyDocks36', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks40 = models.IntegerField(db_column='nbEmptyDocks40', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks48 = models.IntegerField(db_column='nbEmptyDocks48', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks52 = models.IntegerField(db_column='nbEmptyDocks52', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks56 = models.IntegerField(db_column='nbEmptyDocks56', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks60 = models.IntegerField(db_column='nbEmptyDocks60', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks64 = models.IntegerField(db_column='nbEmptyDocks64', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks68 = models.IntegerField(db_column='nbEmptyDocks68', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks72 = models.IntegerField(db_column='nbEmptyDocks72', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks76 = models.IntegerField(db_column='nbEmptyDocks76', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks80 = models.IntegerField(db_column='nbEmptyDocks80', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks84 = models.IntegerField(db_column='nbEmptyDocks84', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks88 = models.IntegerField(db_column='nbEmptyDocks88', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks92 = models.IntegerField(db_column='nbEmptyDocks92', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks96 = models.IntegerField(db_column='nbEmptyDocks96', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks100 = models.IntegerField(db_column='nbEmptyDocks100', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks104 = models.IntegerField(db_column='nbEmptyDocks104', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks108 = models.IntegerField(db_column='nbEmptyDocks108', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks112 = models.IntegerField(db_column='nbEmptyDocks112', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks116 = models.IntegerField(db_column='nbEmptyDocks116', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks120 = models.IntegerField(db_column='nbEmptyDocks120', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks124 = models.IntegerField(db_column='nbEmptyDocks124', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks128 = models.IntegerField(db_column='nbEmptyDocks128', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks132 = models.IntegerField(db_column='nbEmptyDocks132', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks136 = models.IntegerField(db_column='nbEmptyDocks136', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks140 = models.IntegerField(db_column='nbEmptyDocks140', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks144 = models.IntegerField(db_column='nbEmptyDocks144', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks148 = models.IntegerField(db_column='nbEmptyDocks148', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks152 = models.IntegerField(db_column='nbEmptyDocks152', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks156 = models.IntegerField(db_column='nbEmptyDocks156', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks160 = models.IntegerField(db_column='nbEmptyDocks160', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks164 = models.IntegerField(db_column='nbEmptyDocks164', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks168 = models.IntegerField(db_column='nbEmptyDocks168', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks176 = models.IntegerField(db_column='nbEmptyDocks176', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks180 = models.IntegerField(db_column='nbEmptyDocks180', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks184 = models.IntegerField(db_column='nbEmptyDocks184', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks188 = models.IntegerField(db_column='nbEmptyDocks188', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks192 = models.IntegerField(db_column='nbEmptyDocks192', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks196 = models.IntegerField(db_column='nbEmptyDocks196', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks200 = models.IntegerField(db_column='nbEmptyDocks200', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks204 = models.IntegerField(db_column='nbEmptyDocks204', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks208 = models.IntegerField(db_column='nbEmptyDocks208', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks212 = models.IntegerField(db_column='nbEmptyDocks212', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks216 = models.IntegerField(db_column='nbEmptyDocks216', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks220 = models.IntegerField(db_column='nbEmptyDocks220', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks224 = models.IntegerField(db_column='nbEmptyDocks224', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks228 = models.IntegerField(db_column='nbEmptyDocks228', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks232 = models.IntegerField(db_column='nbEmptyDocks232', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks236 = models.IntegerField(db_column='nbEmptyDocks236', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks244 = models.IntegerField(db_column='nbEmptyDocks244', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks248 = models.IntegerField(db_column='nbEmptyDocks248', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks256 = models.IntegerField(db_column='nbEmptyDocks256', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks260 = models.IntegerField(db_column='nbEmptyDocks260', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks264 = models.IntegerField(db_column='nbEmptyDocks264', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks268 = models.IntegerField(db_column='nbEmptyDocks268', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks272 = models.IntegerField(db_column='nbEmptyDocks272', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks276 = models.IntegerField(db_column='nbEmptyDocks276', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks280 = models.IntegerField(db_column='nbEmptyDocks280', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks284 = models.IntegerField(db_column='nbEmptyDocks284', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks288 = models.IntegerField(db_column='nbEmptyDocks288', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks292 = models.IntegerField(db_column='nbEmptyDocks292', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks304 = models.IntegerField(db_column='nbEmptyDocks304', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks308 = models.IntegerField(db_column='nbEmptyDocks308', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks312 = models.IntegerField(db_column='nbEmptyDocks312', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks316 = models.IntegerField(db_column='nbEmptyDocks316', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks320 = models.IntegerField(db_column='nbEmptyDocks320', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks324 = models.IntegerField(db_column='nbEmptyDocks324', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks328 = models.IntegerField(db_column='nbEmptyDocks328', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks332 = models.IntegerField(db_column='nbEmptyDocks332', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks336 = models.IntegerField(db_column='nbEmptyDocks336', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks340 = models.IntegerField(db_column='nbEmptyDocks340', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks344 = models.IntegerField(db_column='nbEmptyDocks344', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks348 = models.IntegerField(db_column='nbEmptyDocks348', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks356 = models.IntegerField(db_column='nbEmptyDocks356', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks360 = models.IntegerField(db_column='nbEmptyDocks360', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks364 = models.IntegerField(db_column='nbEmptyDocks364', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks368 = models.IntegerField(db_column='nbEmptyDocks368', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks372 = models.IntegerField(db_column='nbEmptyDocks372', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks376 = models.IntegerField(db_column='nbEmptyDocks376', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks380 = models.IntegerField(db_column='nbEmptyDocks380', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks384 = models.IntegerField(db_column='nbEmptyDocks384', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks388 = models.IntegerField(db_column='nbEmptyDocks388', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks392 = models.IntegerField(db_column='nbEmptyDocks392', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks396 = models.IntegerField(db_column='nbEmptyDocks396', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks404 = models.IntegerField(db_column='nbEmptyDocks404', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks408 = models.IntegerField(db_column='nbEmptyDocks408', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks416 = models.IntegerField(db_column='nbEmptyDocks416', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks424 = models.IntegerField(db_column='nbEmptyDocks424', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks428 = models.IntegerField(db_column='nbEmptyDocks428', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks432 = models.IntegerField(db_column='nbEmptyDocks432', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks440 = models.IntegerField(db_column='nbEmptyDocks440', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks444 = models.IntegerField(db_column='nbEmptyDocks444', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks448 = models.IntegerField(db_column='nbEmptyDocks448', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks452 = models.IntegerField(db_column='nbEmptyDocks452', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks456 = models.IntegerField(db_column='nbEmptyDocks456', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks460 = models.IntegerField(db_column='nbEmptyDocks460', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks464 = models.IntegerField(db_column='nbEmptyDocks464', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks468 = models.IntegerField(db_column='nbEmptyDocks468', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks472 = models.IntegerField(db_column='nbEmptyDocks472', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks476 = models.IntegerField(db_column='nbEmptyDocks476', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks480 = models.IntegerField(db_column='nbEmptyDocks480', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks484 = models.IntegerField(db_column='nbEmptyDocks484', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks492 = models.IntegerField(db_column='nbEmptyDocks492', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks496 = models.IntegerField(db_column='nbEmptyDocks496', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks500 = models.IntegerField(db_column='nbEmptyDocks500', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'predicted_data_hourly'


# class WeatherData(models.Model):
#     month = models.IntegerField(blank=True, null=True)
#     dayofweek = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     hour = models.IntegerField(blank=True, null=True)
#     icon = models.IntegerField(blank=True, null=True)
#     preciptype = models.IntegerField(db_column='precipType', blank=True, null=True)  # Field name made lowercase.
#     precipintensity = models.TextField(db_column='precipIntensity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     precipprobability = models.TextField(db_column='precipProbability', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     temperature = models.TextField(blank=True, null=True)  # This field type is a guess.
#     apparenttemperature = models.TextField(db_column='apparentTemperature', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     dewpoint = models.TextField(db_column='dewPoint', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     humidity = models.TextField(blank=True, null=True)  # This field type is a guess.
#     windspeed = models.TextField(db_column='windSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     windbearing = models.TextField(db_column='windBearing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     cloudcover = models.TextField(db_column='cloudCover', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     pressure = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ozone = models.TextField(blank=True, null=True)  # This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'weather_data'


# class XDataHourly(models.Model):
#     month = models.IntegerField(blank=True, null=True)
#     dayofweek = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     hour = models.IntegerField(blank=True, null=True)
#     icon = models.IntegerField(blank=True, null=True)
#     preciptype = models.IntegerField(db_column='precipType', blank=True, null=True)  # Field name made lowercase.
#     precipintensity = models.FloatField(db_column='precipIntensity', blank=True, null=True)  # Field name made lowercase.
#     precipprobability = models.FloatField(db_column='precipProbability', blank=True, null=True)  # Field name made lowercase.
#     temperature = models.FloatField(blank=True, null=True)
#     apparenttemperature = models.FloatField(db_column='apparentTemperature', blank=True, null=True)  # Field name made lowercase.
#     dewpoint = models.FloatField(db_column='dewPoint', blank=True, null=True)  # Field name made lowercase.
#     humidity = models.FloatField(blank=True, null=True)
#     windspeed = models.FloatField(db_column='windSpeed', blank=True, null=True)  # Field name made lowercase.
#     windbearing = models.FloatField(db_column='windBearing', blank=True, null=True)  # Field name made lowercase.
#     cloudcover = models.FloatField(db_column='cloudCover', blank=True, null=True)  # Field name made lowercase.
#     pressure = models.FloatField(blank=True, null=True)
#     ozone = models.FloatField(blank=True, null=True)
#     bikes_arrived_4 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_8 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_12 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_16 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_20 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_24 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_28 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_32 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_36 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_40 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_48 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_52 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_56 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_60 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_64 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_68 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_72 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_76 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_80 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_84 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_88 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_92 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_96 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_100 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_104 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_108 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_112 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_116 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_120 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_124 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_128 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_132 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_136 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_140 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_144 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_148 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_152 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_156 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_160 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_164 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_168 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_176 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_180 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_184 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_188 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_192 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_196 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_200 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_204 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_208 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_212 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_216 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_220 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_224 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_228 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_232 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_236 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_244 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_248 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_256 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_260 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_264 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_268 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_272 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_276 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_280 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_284 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_288 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_292 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_304 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_308 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_312 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_316 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_320 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_324 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_328 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_332 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_336 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_340 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_344 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_348 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_356 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_360 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_364 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_368 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_372 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_376 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_380 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_384 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_388 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_392 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_396 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_404 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_408 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_416 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_424 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_428 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_432 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_440 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_444 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_448 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_452 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_456 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_460 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_464 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_468 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_472 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_476 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_480 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_484 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_492 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_496 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_500 = models.IntegerField(blank=True, null=True)
#     bikes_arrived_504 = models.IntegerField(blank=True, null=True)
#     bikes_left_4 = models.IntegerField(blank=True, null=True)
#     bikes_left_8 = models.IntegerField(blank=True, null=True)
#     bikes_left_12 = models.IntegerField(blank=True, null=True)
#     bikes_left_16 = models.IntegerField(blank=True, null=True)
#     bikes_left_20 = models.IntegerField(blank=True, null=True)
#     bikes_left_24 = models.IntegerField(blank=True, null=True)
#     bikes_left_28 = models.IntegerField(blank=True, null=True)
#     bikes_left_32 = models.IntegerField(blank=True, null=True)
#     bikes_left_36 = models.IntegerField(blank=True, null=True)
#     bikes_left_40 = models.IntegerField(blank=True, null=True)
#     bikes_left_48 = models.IntegerField(blank=True, null=True)
#     bikes_left_52 = models.IntegerField(blank=True, null=True)
#     bikes_left_56 = models.IntegerField(blank=True, null=True)
#     bikes_left_60 = models.IntegerField(blank=True, null=True)
#     bikes_left_64 = models.IntegerField(blank=True, null=True)
#     bikes_left_68 = models.IntegerField(blank=True, null=True)
#     bikes_left_72 = models.IntegerField(blank=True, null=True)
#     bikes_left_76 = models.IntegerField(blank=True, null=True)
#     bikes_left_80 = models.IntegerField(blank=True, null=True)
#     bikes_left_84 = models.IntegerField(blank=True, null=True)
#     bikes_left_88 = models.IntegerField(blank=True, null=True)
#     bikes_left_92 = models.IntegerField(blank=True, null=True)
#     bikes_left_96 = models.IntegerField(blank=True, null=True)
#     bikes_left_100 = models.IntegerField(blank=True, null=True)
#     bikes_left_104 = models.IntegerField(blank=True, null=True)
#     bikes_left_108 = models.IntegerField(blank=True, null=True)
#     bikes_left_112 = models.IntegerField(blank=True, null=True)
#     bikes_left_116 = models.IntegerField(blank=True, null=True)
#     bikes_left_120 = models.IntegerField(blank=True, null=True)
#     bikes_left_124 = models.IntegerField(blank=True, null=True)
#     bikes_left_128 = models.IntegerField(blank=True, null=True)
#     bikes_left_132 = models.IntegerField(blank=True, null=True)
#     bikes_left_136 = models.IntegerField(blank=True, null=True)
#     bikes_left_140 = models.IntegerField(blank=True, null=True)
#     bikes_left_144 = models.IntegerField(blank=True, null=True)
#     bikes_left_148 = models.IntegerField(blank=True, null=True)
#     bikes_left_152 = models.IntegerField(blank=True, null=True)
#     bikes_left_156 = models.IntegerField(blank=True, null=True)
#     bikes_left_160 = models.IntegerField(blank=True, null=True)
#     bikes_left_164 = models.IntegerField(blank=True, null=True)
#     bikes_left_168 = models.IntegerField(blank=True, null=True)
#     bikes_left_176 = models.IntegerField(blank=True, null=True)
#     bikes_left_180 = models.IntegerField(blank=True, null=True)
#     bikes_left_184 = models.IntegerField(blank=True, null=True)
#     bikes_left_188 = models.IntegerField(blank=True, null=True)
#     bikes_left_192 = models.IntegerField(blank=True, null=True)
#     bikes_left_196 = models.IntegerField(blank=True, null=True)
#     bikes_left_200 = models.IntegerField(blank=True, null=True)
#     bikes_left_204 = models.IntegerField(blank=True, null=True)
#     bikes_left_208 = models.IntegerField(blank=True, null=True)
#     bikes_left_212 = models.IntegerField(blank=True, null=True)
#     bikes_left_216 = models.IntegerField(blank=True, null=True)
#     bikes_left_220 = models.IntegerField(blank=True, null=True)
#     bikes_left_224 = models.IntegerField(blank=True, null=True)
#     bikes_left_228 = models.IntegerField(blank=True, null=True)
#     bikes_left_232 = models.IntegerField(blank=True, null=True)
#     bikes_left_236 = models.IntegerField(blank=True, null=True)
#     bikes_left_244 = models.IntegerField(blank=True, null=True)
#     bikes_left_248 = models.IntegerField(blank=True, null=True)
#     bikes_left_256 = models.IntegerField(blank=True, null=True)
#     bikes_left_260 = models.IntegerField(blank=True, null=True)
#     bikes_left_264 = models.IntegerField(blank=True, null=True)
#     bikes_left_268 = models.IntegerField(blank=True, null=True)
#     bikes_left_272 = models.IntegerField(blank=True, null=True)
#     bikes_left_276 = models.IntegerField(blank=True, null=True)
#     bikes_left_280 = models.IntegerField(blank=True, null=True)
#     bikes_left_284 = models.IntegerField(blank=True, null=True)
#     bikes_left_288 = models.IntegerField(blank=True, null=True)
#     bikes_left_292 = models.IntegerField(blank=True, null=True)
#     bikes_left_304 = models.IntegerField(blank=True, null=True)
#     bikes_left_308 = models.IntegerField(blank=True, null=True)
#     bikes_left_312 = models.IntegerField(blank=True, null=True)
#     bikes_left_316 = models.IntegerField(blank=True, null=True)
#     bikes_left_320 = models.IntegerField(blank=True, null=True)
#     bikes_left_324 = models.IntegerField(blank=True, null=True)
#     bikes_left_328 = models.IntegerField(blank=True, null=True)
#     bikes_left_332 = models.IntegerField(blank=True, null=True)
#     bikes_left_336 = models.IntegerField(blank=True, null=True)
#     bikes_left_340 = models.IntegerField(blank=True, null=True)
#     bikes_left_344 = models.IntegerField(blank=True, null=True)
#     bikes_left_348 = models.IntegerField(blank=True, null=True)
#     bikes_left_356 = models.IntegerField(blank=True, null=True)
#     bikes_left_360 = models.IntegerField(blank=True, null=True)
#     bikes_left_364 = models.IntegerField(blank=True, null=True)
#     bikes_left_368 = models.IntegerField(blank=True, null=True)
#     bikes_left_372 = models.IntegerField(blank=True, null=True)
#     bikes_left_376 = models.IntegerField(blank=True, null=True)
#     bikes_left_380 = models.IntegerField(blank=True, null=True)
#     bikes_left_384 = models.IntegerField(blank=True, null=True)
#     bikes_left_388 = models.IntegerField(blank=True, null=True)
#     bikes_left_392 = models.IntegerField(blank=True, null=True)
#     bikes_left_396 = models.IntegerField(blank=True, null=True)
#     bikes_left_404 = models.IntegerField(blank=True, null=True)
#     bikes_left_408 = models.IntegerField(blank=True, null=True)
#     bikes_left_416 = models.IntegerField(blank=True, null=True)
#     bikes_left_424 = models.IntegerField(blank=True, null=True)
#     bikes_left_428 = models.IntegerField(blank=True, null=True)
#     bikes_left_432 = models.IntegerField(blank=True, null=True)
#     bikes_left_440 = models.IntegerField(blank=True, null=True)
#     bikes_left_444 = models.IntegerField(blank=True, null=True)
#     bikes_left_448 = models.IntegerField(blank=True, null=True)
#     bikes_left_452 = models.IntegerField(blank=True, null=True)
#     bikes_left_456 = models.IntegerField(blank=True, null=True)
#     bikes_left_460 = models.IntegerField(blank=True, null=True)
#     bikes_left_464 = models.IntegerField(blank=True, null=True)
#     bikes_left_468 = models.IntegerField(blank=True, null=True)
#     bikes_left_472 = models.IntegerField(blank=True, null=True)
#     bikes_left_476 = models.IntegerField(blank=True, null=True)
#     bikes_left_480 = models.IntegerField(blank=True, null=True)
#     bikes_left_484 = models.IntegerField(blank=True, null=True)
#     bikes_left_492 = models.IntegerField(blank=True, null=True)
#     bikes_left_496 = models.IntegerField(blank=True, null=True)
#     bikes_left_500 = models.IntegerField(blank=True, null=True)
#     bikes_left_504 = models.IntegerField(blank=True, null=True)
#     month_1 = models.IntegerField(db_column='month:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
#     day_1 = models.IntegerField(db_column='day:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
#     hour_1 = models.IntegerField(db_column='hour:1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
#     nbbikes4 = models.IntegerField(db_column='nbBikes4', blank=True, null=True)  # Field name made lowercase.
#     nbbikes8 = models.IntegerField(db_column='nbBikes8', blank=True, null=True)  # Field name made lowercase.
#     nbbikes12 = models.IntegerField(db_column='nbBikes12', blank=True, null=True)  # Field name made lowercase.
#     nbbikes16 = models.IntegerField(db_column='nbBikes16', blank=True, null=True)  # Field name made lowercase.
#     nbbikes20 = models.IntegerField(db_column='nbBikes20', blank=True, null=True)  # Field name made lowercase.
#     nbbikes24 = models.IntegerField(db_column='nbBikes24', blank=True, null=True)  # Field name made lowercase.
#     nbbikes28 = models.IntegerField(db_column='nbBikes28', blank=True, null=True)  # Field name made lowercase.
#     nbbikes32 = models.IntegerField(db_column='nbBikes32', blank=True, null=True)  # Field name made lowercase.
#     nbbikes36 = models.IntegerField(db_column='nbBikes36', blank=True, null=True)  # Field name made lowercase.
#     nbbikes40 = models.IntegerField(db_column='nbBikes40', blank=True, null=True)  # Field name made lowercase.
#     nbbikes48 = models.IntegerField(db_column='nbBikes48', blank=True, null=True)  # Field name made lowercase.
#     nbbikes52 = models.IntegerField(db_column='nbBikes52', blank=True, null=True)  # Field name made lowercase.
#     nbbikes56 = models.IntegerField(db_column='nbBikes56', blank=True, null=True)  # Field name made lowercase.
#     nbbikes60 = models.IntegerField(db_column='nbBikes60', blank=True, null=True)  # Field name made lowercase.
#     nbbikes64 = models.IntegerField(db_column='nbBikes64', blank=True, null=True)  # Field name made lowercase.
#     nbbikes68 = models.IntegerField(db_column='nbBikes68', blank=True, null=True)  # Field name made lowercase.
#     nbbikes72 = models.IntegerField(db_column='nbBikes72', blank=True, null=True)  # Field name made lowercase.
#     nbbikes76 = models.IntegerField(db_column='nbBikes76', blank=True, null=True)  # Field name made lowercase.
#     nbbikes80 = models.IntegerField(db_column='nbBikes80', blank=True, null=True)  # Field name made lowercase.
#     nbbikes84 = models.IntegerField(db_column='nbBikes84', blank=True, null=True)  # Field name made lowercase.
#     nbbikes88 = models.IntegerField(db_column='nbBikes88', blank=True, null=True)  # Field name made lowercase.
#     nbbikes92 = models.IntegerField(db_column='nbBikes92', blank=True, null=True)  # Field name made lowercase.
#     nbbikes96 = models.IntegerField(db_column='nbBikes96', blank=True, null=True)  # Field name made lowercase.
#     nbbikes100 = models.IntegerField(db_column='nbBikes100', blank=True, null=True)  # Field name made lowercase.
#     nbbikes104 = models.IntegerField(db_column='nbBikes104', blank=True, null=True)  # Field name made lowercase.
#     nbbikes108 = models.IntegerField(db_column='nbBikes108', blank=True, null=True)  # Field name made lowercase.
#     nbbikes112 = models.IntegerField(db_column='nbBikes112', blank=True, null=True)  # Field name made lowercase.
#     nbbikes116 = models.IntegerField(db_column='nbBikes116', blank=True, null=True)  # Field name made lowercase.
#     nbbikes120 = models.IntegerField(db_column='nbBikes120', blank=True, null=True)  # Field name made lowercase.
#     nbbikes124 = models.IntegerField(db_column='nbBikes124', blank=True, null=True)  # Field name made lowercase.
#     nbbikes128 = models.IntegerField(db_column='nbBikes128', blank=True, null=True)  # Field name made lowercase.
#     nbbikes132 = models.IntegerField(db_column='nbBikes132', blank=True, null=True)  # Field name made lowercase.
#     nbbikes136 = models.IntegerField(db_column='nbBikes136', blank=True, null=True)  # Field name made lowercase.
#     nbbikes140 = models.IntegerField(db_column='nbBikes140', blank=True, null=True)  # Field name made lowercase.
#     nbbikes144 = models.IntegerField(db_column='nbBikes144', blank=True, null=True)  # Field name made lowercase.
#     nbbikes148 = models.IntegerField(db_column='nbBikes148', blank=True, null=True)  # Field name made lowercase.
#     nbbikes152 = models.IntegerField(db_column='nbBikes152', blank=True, null=True)  # Field name made lowercase.
#     nbbikes156 = models.IntegerField(db_column='nbBikes156', blank=True, null=True)  # Field name made lowercase.
#     nbbikes160 = models.IntegerField(db_column='nbBikes160', blank=True, null=True)  # Field name made lowercase.
#     nbbikes164 = models.IntegerField(db_column='nbBikes164', blank=True, null=True)  # Field name made lowercase.
#     nbbikes168 = models.IntegerField(db_column='nbBikes168', blank=True, null=True)  # Field name made lowercase.
#     nbbikes176 = models.IntegerField(db_column='nbBikes176', blank=True, null=True)  # Field name made lowercase.
#     nbbikes180 = models.IntegerField(db_column='nbBikes180', blank=True, null=True)  # Field name made lowercase.
#     nbbikes184 = models.IntegerField(db_column='nbBikes184', blank=True, null=True)  # Field name made lowercase.
#     nbbikes188 = models.IntegerField(db_column='nbBikes188', blank=True, null=True)  # Field name made lowercase.
#     nbbikes192 = models.IntegerField(db_column='nbBikes192', blank=True, null=True)  # Field name made lowercase.
#     nbbikes196 = models.IntegerField(db_column='nbBikes196', blank=True, null=True)  # Field name made lowercase.
#     nbbikes200 = models.IntegerField(db_column='nbBikes200', blank=True, null=True)  # Field name made lowercase.
#     nbbikes204 = models.IntegerField(db_column='nbBikes204', blank=True, null=True)  # Field name made lowercase.
#     nbbikes208 = models.IntegerField(db_column='nbBikes208', blank=True, null=True)  # Field name made lowercase.
#     nbbikes212 = models.IntegerField(db_column='nbBikes212', blank=True, null=True)  # Field name made lowercase.
#     nbbikes216 = models.IntegerField(db_column='nbBikes216', blank=True, null=True)  # Field name made lowercase.
#     nbbikes220 = models.IntegerField(db_column='nbBikes220', blank=True, null=True)  # Field name made lowercase.
#     nbbikes224 = models.IntegerField(db_column='nbBikes224', blank=True, null=True)  # Field name made lowercase.
#     nbbikes228 = models.IntegerField(db_column='nbBikes228', blank=True, null=True)  # Field name made lowercase.
#     nbbikes232 = models.IntegerField(db_column='nbBikes232', blank=True, null=True)  # Field name made lowercase.
#     nbbikes236 = models.IntegerField(db_column='nbBikes236', blank=True, null=True)  # Field name made lowercase.
#     nbbikes244 = models.IntegerField(db_column='nbBikes244', blank=True, null=True)  # Field name made lowercase.
#     nbbikes248 = models.IntegerField(db_column='nbBikes248', blank=True, null=True)  # Field name made lowercase.
#     nbbikes256 = models.IntegerField(db_column='nbBikes256', blank=True, null=True)  # Field name made lowercase.
#     nbbikes260 = models.IntegerField(db_column='nbBikes260', blank=True, null=True)  # Field name made lowercase.
#     nbbikes264 = models.IntegerField(db_column='nbBikes264', blank=True, null=True)  # Field name made lowercase.
#     nbbikes268 = models.IntegerField(db_column='nbBikes268', blank=True, null=True)  # Field name made lowercase.
#     nbbikes272 = models.IntegerField(db_column='nbBikes272', blank=True, null=True)  # Field name made lowercase.
#     nbbikes276 = models.IntegerField(db_column='nbBikes276', blank=True, null=True)  # Field name made lowercase.
#     nbbikes280 = models.IntegerField(db_column='nbBikes280', blank=True, null=True)  # Field name made lowercase.
#     nbbikes284 = models.IntegerField(db_column='nbBikes284', blank=True, null=True)  # Field name made lowercase.
#     nbbikes288 = models.IntegerField(db_column='nbBikes288', blank=True, null=True)  # Field name made lowercase.
#     nbbikes292 = models.IntegerField(db_column='nbBikes292', blank=True, null=True)  # Field name made lowercase.
#     nbbikes304 = models.IntegerField(db_column='nbBikes304', blank=True, null=True)  # Field name made lowercase.
#     nbbikes308 = models.IntegerField(db_column='nbBikes308', blank=True, null=True)  # Field name made lowercase.
#     nbbikes312 = models.IntegerField(db_column='nbBikes312', blank=True, null=True)  # Field name made lowercase.
#     nbbikes316 = models.IntegerField(db_column='nbBikes316', blank=True, null=True)  # Field name made lowercase.
#     nbbikes320 = models.IntegerField(db_column='nbBikes320', blank=True, null=True)  # Field name made lowercase.
#     nbbikes324 = models.IntegerField(db_column='nbBikes324', blank=True, null=True)  # Field name made lowercase.
#     nbbikes328 = models.IntegerField(db_column='nbBikes328', blank=True, null=True)  # Field name made lowercase.
#     nbbikes332 = models.IntegerField(db_column='nbBikes332', blank=True, null=True)  # Field name made lowercase.
#     nbbikes336 = models.IntegerField(db_column='nbBikes336', blank=True, null=True)  # Field name made lowercase.
#     nbbikes340 = models.IntegerField(db_column='nbBikes340', blank=True, null=True)  # Field name made lowercase.
#     nbbikes344 = models.IntegerField(db_column='nbBikes344', blank=True, null=True)  # Field name made lowercase.
#     nbbikes348 = models.IntegerField(db_column='nbBikes348', blank=True, null=True)  # Field name made lowercase.
#     nbbikes356 = models.IntegerField(db_column='nbBikes356', blank=True, null=True)  # Field name made lowercase.
#     nbbikes360 = models.IntegerField(db_column='nbBikes360', blank=True, null=True)  # Field name made lowercase.
#     nbbikes364 = models.IntegerField(db_column='nbBikes364', blank=True, null=True)  # Field name made lowercase.
#     nbbikes368 = models.IntegerField(db_column='nbBikes368', blank=True, null=True)  # Field name made lowercase.
#     nbbikes372 = models.IntegerField(db_column='nbBikes372', blank=True, null=True)  # Field name made lowercase.
#     nbbikes376 = models.IntegerField(db_column='nbBikes376', blank=True, null=True)  # Field name made lowercase.
#     nbbikes380 = models.IntegerField(db_column='nbBikes380', blank=True, null=True)  # Field name made lowercase.
#     nbbikes384 = models.IntegerField(db_column='nbBikes384', blank=True, null=True)  # Field name made lowercase.
#     nbbikes388 = models.IntegerField(db_column='nbBikes388', blank=True, null=True)  # Field name made lowercase.
#     nbbikes392 = models.IntegerField(db_column='nbBikes392', blank=True, null=True)  # Field name made lowercase.
#     nbbikes396 = models.IntegerField(db_column='nbBikes396', blank=True, null=True)  # Field name made lowercase.
#     nbbikes404 = models.IntegerField(db_column='nbBikes404', blank=True, null=True)  # Field name made lowercase.
#     nbbikes408 = models.IntegerField(db_column='nbBikes408', blank=True, null=True)  # Field name made lowercase.
#     nbbikes416 = models.IntegerField(db_column='nbBikes416', blank=True, null=True)  # Field name made lowercase.
#     nbbikes424 = models.IntegerField(db_column='nbBikes424', blank=True, null=True)  # Field name made lowercase.
#     nbbikes428 = models.IntegerField(db_column='nbBikes428', blank=True, null=True)  # Field name made lowercase.
#     nbbikes432 = models.IntegerField(db_column='nbBikes432', blank=True, null=True)  # Field name made lowercase.
#     nbbikes440 = models.IntegerField(db_column='nbBikes440', blank=True, null=True)  # Field name made lowercase.
#     nbbikes444 = models.IntegerField(db_column='nbBikes444', blank=True, null=True)  # Field name made lowercase.
#     nbbikes448 = models.IntegerField(db_column='nbBikes448', blank=True, null=True)  # Field name made lowercase.
#     nbbikes452 = models.IntegerField(db_column='nbBikes452', blank=True, null=True)  # Field name made lowercase.
#     nbbikes456 = models.IntegerField(db_column='nbBikes456', blank=True, null=True)  # Field name made lowercase.
#     nbbikes460 = models.IntegerField(db_column='nbBikes460', blank=True, null=True)  # Field name made lowercase.
#     nbbikes464 = models.IntegerField(db_column='nbBikes464', blank=True, null=True)  # Field name made lowercase.
#     nbbikes468 = models.IntegerField(db_column='nbBikes468', blank=True, null=True)  # Field name made lowercase.
#     nbbikes472 = models.IntegerField(db_column='nbBikes472', blank=True, null=True)  # Field name made lowercase.
#     nbbikes476 = models.IntegerField(db_column='nbBikes476', blank=True, null=True)  # Field name made lowercase.
#     nbbikes480 = models.IntegerField(db_column='nbBikes480', blank=True, null=True)  # Field name made lowercase.
#     nbbikes484 = models.IntegerField(db_column='nbBikes484', blank=True, null=True)  # Field name made lowercase.
#     nbbikes492 = models.IntegerField(db_column='nbBikes492', blank=True, null=True)  # Field name made lowercase.
#     nbbikes496 = models.IntegerField(db_column='nbBikes496', blank=True, null=True)  # Field name made lowercase.
#     nbbikes500 = models.IntegerField(db_column='nbBikes500', blank=True, null=True)  # Field name made lowercase.
#     nbbikes504 = models.IntegerField(db_column='nbBikes504', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks4 = models.IntegerField(db_column='nbEmptyDocks4', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks8 = models.IntegerField(db_column='nbEmptyDocks8', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks12 = models.IntegerField(db_column='nbEmptyDocks12', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks16 = models.IntegerField(db_column='nbEmptyDocks16', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks20 = models.IntegerField(db_column='nbEmptyDocks20', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks24 = models.IntegerField(db_column='nbEmptyDocks24', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks28 = models.IntegerField(db_column='nbEmptyDocks28', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks32 = models.IntegerField(db_column='nbEmptyDocks32', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks36 = models.IntegerField(db_column='nbEmptyDocks36', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks40 = models.IntegerField(db_column='nbEmptyDocks40', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks48 = models.IntegerField(db_column='nbEmptyDocks48', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks52 = models.IntegerField(db_column='nbEmptyDocks52', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks56 = models.IntegerField(db_column='nbEmptyDocks56', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks60 = models.IntegerField(db_column='nbEmptyDocks60', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks64 = models.IntegerField(db_column='nbEmptyDocks64', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks68 = models.IntegerField(db_column='nbEmptyDocks68', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks72 = models.IntegerField(db_column='nbEmptyDocks72', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks76 = models.IntegerField(db_column='nbEmptyDocks76', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks80 = models.IntegerField(db_column='nbEmptyDocks80', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks84 = models.IntegerField(db_column='nbEmptyDocks84', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks88 = models.IntegerField(db_column='nbEmptyDocks88', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks92 = models.IntegerField(db_column='nbEmptyDocks92', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks96 = models.IntegerField(db_column='nbEmptyDocks96', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks100 = models.IntegerField(db_column='nbEmptyDocks100', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks104 = models.IntegerField(db_column='nbEmptyDocks104', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks108 = models.IntegerField(db_column='nbEmptyDocks108', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks112 = models.IntegerField(db_column='nbEmptyDocks112', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks116 = models.IntegerField(db_column='nbEmptyDocks116', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks120 = models.IntegerField(db_column='nbEmptyDocks120', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks124 = models.IntegerField(db_column='nbEmptyDocks124', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks128 = models.IntegerField(db_column='nbEmptyDocks128', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks132 = models.IntegerField(db_column='nbEmptyDocks132', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks136 = models.IntegerField(db_column='nbEmptyDocks136', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks140 = models.IntegerField(db_column='nbEmptyDocks140', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks144 = models.IntegerField(db_column='nbEmptyDocks144', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks148 = models.IntegerField(db_column='nbEmptyDocks148', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks152 = models.IntegerField(db_column='nbEmptyDocks152', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks156 = models.IntegerField(db_column='nbEmptyDocks156', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks160 = models.IntegerField(db_column='nbEmptyDocks160', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks164 = models.IntegerField(db_column='nbEmptyDocks164', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks168 = models.IntegerField(db_column='nbEmptyDocks168', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks176 = models.IntegerField(db_column='nbEmptyDocks176', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks180 = models.IntegerField(db_column='nbEmptyDocks180', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks184 = models.IntegerField(db_column='nbEmptyDocks184', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks188 = models.IntegerField(db_column='nbEmptyDocks188', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks192 = models.IntegerField(db_column='nbEmptyDocks192', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks196 = models.IntegerField(db_column='nbEmptyDocks196', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks200 = models.IntegerField(db_column='nbEmptyDocks200', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks204 = models.IntegerField(db_column='nbEmptyDocks204', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks208 = models.IntegerField(db_column='nbEmptyDocks208', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks212 = models.IntegerField(db_column='nbEmptyDocks212', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks216 = models.IntegerField(db_column='nbEmptyDocks216', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks220 = models.IntegerField(db_column='nbEmptyDocks220', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks224 = models.IntegerField(db_column='nbEmptyDocks224', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks228 = models.IntegerField(db_column='nbEmptyDocks228', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks232 = models.IntegerField(db_column='nbEmptyDocks232', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks236 = models.IntegerField(db_column='nbEmptyDocks236', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks244 = models.IntegerField(db_column='nbEmptyDocks244', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks248 = models.IntegerField(db_column='nbEmptyDocks248', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks256 = models.IntegerField(db_column='nbEmptyDocks256', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks260 = models.IntegerField(db_column='nbEmptyDocks260', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks264 = models.IntegerField(db_column='nbEmptyDocks264', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks268 = models.IntegerField(db_column='nbEmptyDocks268', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks272 = models.IntegerField(db_column='nbEmptyDocks272', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks276 = models.IntegerField(db_column='nbEmptyDocks276', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks280 = models.IntegerField(db_column='nbEmptyDocks280', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks284 = models.IntegerField(db_column='nbEmptyDocks284', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks288 = models.IntegerField(db_column='nbEmptyDocks288', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks292 = models.IntegerField(db_column='nbEmptyDocks292', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks304 = models.IntegerField(db_column='nbEmptyDocks304', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks308 = models.IntegerField(db_column='nbEmptyDocks308', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks312 = models.IntegerField(db_column='nbEmptyDocks312', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks316 = models.IntegerField(db_column='nbEmptyDocks316', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks320 = models.IntegerField(db_column='nbEmptyDocks320', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks324 = models.IntegerField(db_column='nbEmptyDocks324', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks328 = models.IntegerField(db_column='nbEmptyDocks328', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks332 = models.IntegerField(db_column='nbEmptyDocks332', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks336 = models.IntegerField(db_column='nbEmptyDocks336', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks340 = models.IntegerField(db_column='nbEmptyDocks340', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks344 = models.IntegerField(db_column='nbEmptyDocks344', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks348 = models.IntegerField(db_column='nbEmptyDocks348', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks356 = models.IntegerField(db_column='nbEmptyDocks356', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks360 = models.IntegerField(db_column='nbEmptyDocks360', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks364 = models.IntegerField(db_column='nbEmptyDocks364', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks368 = models.IntegerField(db_column='nbEmptyDocks368', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks372 = models.IntegerField(db_column='nbEmptyDocks372', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks376 = models.IntegerField(db_column='nbEmptyDocks376', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks380 = models.IntegerField(db_column='nbEmptyDocks380', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks384 = models.IntegerField(db_column='nbEmptyDocks384', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks388 = models.IntegerField(db_column='nbEmptyDocks388', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks392 = models.IntegerField(db_column='nbEmptyDocks392', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks396 = models.IntegerField(db_column='nbEmptyDocks396', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks404 = models.IntegerField(db_column='nbEmptyDocks404', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks408 = models.IntegerField(db_column='nbEmptyDocks408', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks416 = models.IntegerField(db_column='nbEmptyDocks416', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks424 = models.IntegerField(db_column='nbEmptyDocks424', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks428 = models.IntegerField(db_column='nbEmptyDocks428', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks432 = models.IntegerField(db_column='nbEmptyDocks432', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks440 = models.IntegerField(db_column='nbEmptyDocks440', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks444 = models.IntegerField(db_column='nbEmptyDocks444', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks448 = models.IntegerField(db_column='nbEmptyDocks448', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks452 = models.IntegerField(db_column='nbEmptyDocks452', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks456 = models.IntegerField(db_column='nbEmptyDocks456', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks460 = models.IntegerField(db_column='nbEmptyDocks460', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks464 = models.IntegerField(db_column='nbEmptyDocks464', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks468 = models.IntegerField(db_column='nbEmptyDocks468', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks472 = models.IntegerField(db_column='nbEmptyDocks472', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks476 = models.IntegerField(db_column='nbEmptyDocks476', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks480 = models.IntegerField(db_column='nbEmptyDocks480', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks484 = models.IntegerField(db_column='nbEmptyDocks484', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks492 = models.IntegerField(db_column='nbEmptyDocks492', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks496 = models.IntegerField(db_column='nbEmptyDocks496', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks500 = models.IntegerField(db_column='nbEmptyDocks500', blank=True, null=True)  # Field name made lowercase.
#     nbemptydocks504 = models.IntegerField(db_column='nbEmptyDocks504', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'x_data_hourly'


class YDataHourly(models.Model):
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    nbbikes4 = models.IntegerField(db_column='nbBikes4', blank=True, null=True)  # Field name made lowercase.
    nbbikes8 = models.IntegerField(db_column='nbBikes8', blank=True, null=True)  # Field name made lowercase.
    nbbikes12 = models.IntegerField(db_column='nbBikes12', blank=True, null=True)  # Field name made lowercase.
    nbbikes16 = models.IntegerField(db_column='nbBikes16', blank=True, null=True)  # Field name made lowercase.
    nbbikes20 = models.IntegerField(db_column='nbBikes20', blank=True, null=True)  # Field name made lowercase.
    nbbikes24 = models.IntegerField(db_column='nbBikes24', blank=True, null=True)  # Field name made lowercase.
    nbbikes28 = models.IntegerField(db_column='nbBikes28', blank=True, null=True)  # Field name made lowercase.
    nbbikes32 = models.IntegerField(db_column='nbBikes32', blank=True, null=True)  # Field name made lowercase.
    nbbikes36 = models.IntegerField(db_column='nbBikes36', blank=True, null=True)  # Field name made lowercase.
    nbbikes40 = models.IntegerField(db_column='nbBikes40', blank=True, null=True)  # Field name made lowercase.
    nbbikes48 = models.IntegerField(db_column='nbBikes48', blank=True, null=True)  # Field name made lowercase.
    nbbikes52 = models.IntegerField(db_column='nbBikes52', blank=True, null=True)  # Field name made lowercase.
    nbbikes56 = models.IntegerField(db_column='nbBikes56', blank=True, null=True)  # Field name made lowercase.
    nbbikes60 = models.IntegerField(db_column='nbBikes60', blank=True, null=True)  # Field name made lowercase.
    nbbikes64 = models.IntegerField(db_column='nbBikes64', blank=True, null=True)  # Field name made lowercase.
    nbbikes68 = models.IntegerField(db_column='nbBikes68', blank=True, null=True)  # Field name made lowercase.
    nbbikes72 = models.IntegerField(db_column='nbBikes72', blank=True, null=True)  # Field name made lowercase.
    nbbikes76 = models.IntegerField(db_column='nbBikes76', blank=True, null=True)  # Field name made lowercase.
    nbbikes80 = models.IntegerField(db_column='nbBikes80', blank=True, null=True)  # Field name made lowercase.
    nbbikes84 = models.IntegerField(db_column='nbBikes84', blank=True, null=True)  # Field name made lowercase.
    nbbikes88 = models.IntegerField(db_column='nbBikes88', blank=True, null=True)  # Field name made lowercase.
    nbbikes92 = models.IntegerField(db_column='nbBikes92', blank=True, null=True)  # Field name made lowercase.
    nbbikes96 = models.IntegerField(db_column='nbBikes96', blank=True, null=True)  # Field name made lowercase.
    nbbikes100 = models.IntegerField(db_column='nbBikes100', blank=True, null=True)  # Field name made lowercase.
    nbbikes104 = models.IntegerField(db_column='nbBikes104', blank=True, null=True)  # Field name made lowercase.
    nbbikes108 = models.IntegerField(db_column='nbBikes108', blank=True, null=True)  # Field name made lowercase.
    nbbikes112 = models.IntegerField(db_column='nbBikes112', blank=True, null=True)  # Field name made lowercase.
    nbbikes116 = models.IntegerField(db_column='nbBikes116', blank=True, null=True)  # Field name made lowercase.
    nbbikes120 = models.IntegerField(db_column='nbBikes120', blank=True, null=True)  # Field name made lowercase.
    nbbikes124 = models.IntegerField(db_column='nbBikes124', blank=True, null=True)  # Field name made lowercase.
    nbbikes128 = models.IntegerField(db_column='nbBikes128', blank=True, null=True)  # Field name made lowercase.
    nbbikes132 = models.IntegerField(db_column='nbBikes132', blank=True, null=True)  # Field name made lowercase.
    nbbikes136 = models.IntegerField(db_column='nbBikes136', blank=True, null=True)  # Field name made lowercase.
    nbbikes140 = models.IntegerField(db_column='nbBikes140', blank=True, null=True)  # Field name made lowercase.
    nbbikes144 = models.IntegerField(db_column='nbBikes144', blank=True, null=True)  # Field name made lowercase.
    nbbikes148 = models.IntegerField(db_column='nbBikes148', blank=True, null=True)  # Field name made lowercase.
    nbbikes152 = models.IntegerField(db_column='nbBikes152', blank=True, null=True)  # Field name made lowercase.
    nbbikes156 = models.IntegerField(db_column='nbBikes156', blank=True, null=True)  # Field name made lowercase.
    nbbikes160 = models.IntegerField(db_column='nbBikes160', blank=True, null=True)  # Field name made lowercase.
    nbbikes164 = models.IntegerField(db_column='nbBikes164', blank=True, null=True)  # Field name made lowercase.
    nbbikes168 = models.IntegerField(db_column='nbBikes168', blank=True, null=True)  # Field name made lowercase.
    nbbikes176 = models.IntegerField(db_column='nbBikes176', blank=True, null=True)  # Field name made lowercase.
    nbbikes180 = models.IntegerField(db_column='nbBikes180', blank=True, null=True)  # Field name made lowercase.
    nbbikes184 = models.IntegerField(db_column='nbBikes184', blank=True, null=True)  # Field name made lowercase.
    nbbikes188 = models.IntegerField(db_column='nbBikes188', blank=True, null=True)  # Field name made lowercase.
    nbbikes192 = models.IntegerField(db_column='nbBikes192', blank=True, null=True)  # Field name made lowercase.
    nbbikes196 = models.IntegerField(db_column='nbBikes196', blank=True, null=True)  # Field name made lowercase.
    nbbikes200 = models.IntegerField(db_column='nbBikes200', blank=True, null=True)  # Field name made lowercase.
    nbbikes204 = models.IntegerField(db_column='nbBikes204', blank=True, null=True)  # Field name made lowercase.
    nbbikes208 = models.IntegerField(db_column='nbBikes208', blank=True, null=True)  # Field name made lowercase.
    nbbikes212 = models.IntegerField(db_column='nbBikes212', blank=True, null=True)  # Field name made lowercase.
    nbbikes216 = models.IntegerField(db_column='nbBikes216', blank=True, null=True)  # Field name made lowercase.
    nbbikes220 = models.IntegerField(db_column='nbBikes220', blank=True, null=True)  # Field name made lowercase.
    nbbikes224 = models.IntegerField(db_column='nbBikes224', blank=True, null=True)  # Field name made lowercase.
    nbbikes228 = models.IntegerField(db_column='nbBikes228', blank=True, null=True)  # Field name made lowercase.
    nbbikes232 = models.IntegerField(db_column='nbBikes232', blank=True, null=True)  # Field name made lowercase.
    nbbikes236 = models.IntegerField(db_column='nbBikes236', blank=True, null=True)  # Field name made lowercase.
    nbbikes244 = models.IntegerField(db_column='nbBikes244', blank=True, null=True)  # Field name made lowercase.
    nbbikes248 = models.IntegerField(db_column='nbBikes248', blank=True, null=True)  # Field name made lowercase.
    nbbikes256 = models.IntegerField(db_column='nbBikes256', blank=True, null=True)  # Field name made lowercase.
    nbbikes260 = models.IntegerField(db_column='nbBikes260', blank=True, null=True)  # Field name made lowercase.
    nbbikes264 = models.IntegerField(db_column='nbBikes264', blank=True, null=True)  # Field name made lowercase.
    nbbikes268 = models.IntegerField(db_column='nbBikes268', blank=True, null=True)  # Field name made lowercase.
    nbbikes272 = models.IntegerField(db_column='nbBikes272', blank=True, null=True)  # Field name made lowercase.
    nbbikes276 = models.IntegerField(db_column='nbBikes276', blank=True, null=True)  # Field name made lowercase.
    nbbikes280 = models.IntegerField(db_column='nbBikes280', blank=True, null=True)  # Field name made lowercase.
    nbbikes284 = models.IntegerField(db_column='nbBikes284', blank=True, null=True)  # Field name made lowercase.
    nbbikes288 = models.IntegerField(db_column='nbBikes288', blank=True, null=True)  # Field name made lowercase.
    nbbikes292 = models.IntegerField(db_column='nbBikes292', blank=True, null=True)  # Field name made lowercase.
    nbbikes304 = models.IntegerField(db_column='nbBikes304', blank=True, null=True)  # Field name made lowercase.
    nbbikes308 = models.IntegerField(db_column='nbBikes308', blank=True, null=True)  # Field name made lowercase.
    nbbikes312 = models.IntegerField(db_column='nbBikes312', blank=True, null=True)  # Field name made lowercase.
    nbbikes316 = models.IntegerField(db_column='nbBikes316', blank=True, null=True)  # Field name made lowercase.
    nbbikes320 = models.IntegerField(db_column='nbBikes320', blank=True, null=True)  # Field name made lowercase.
    nbbikes324 = models.IntegerField(db_column='nbBikes324', blank=True, null=True)  # Field name made lowercase.
    nbbikes328 = models.IntegerField(db_column='nbBikes328', blank=True, null=True)  # Field name made lowercase.
    nbbikes332 = models.IntegerField(db_column='nbBikes332', blank=True, null=True)  # Field name made lowercase.
    nbbikes336 = models.IntegerField(db_column='nbBikes336', blank=True, null=True)  # Field name made lowercase.
    nbbikes340 = models.IntegerField(db_column='nbBikes340', blank=True, null=True)  # Field name made lowercase.
    nbbikes344 = models.IntegerField(db_column='nbBikes344', blank=True, null=True)  # Field name made lowercase.
    nbbikes348 = models.IntegerField(db_column='nbBikes348', blank=True, null=True)  # Field name made lowercase.
    nbbikes356 = models.IntegerField(db_column='nbBikes356', blank=True, null=True)  # Field name made lowercase.
    nbbikes360 = models.IntegerField(db_column='nbBikes360', blank=True, null=True)  # Field name made lowercase.
    nbbikes364 = models.IntegerField(db_column='nbBikes364', blank=True, null=True)  # Field name made lowercase.
    nbbikes368 = models.IntegerField(db_column='nbBikes368', blank=True, null=True)  # Field name made lowercase.
    nbbikes372 = models.IntegerField(db_column='nbBikes372', blank=True, null=True)  # Field name made lowercase.
    nbbikes376 = models.IntegerField(db_column='nbBikes376', blank=True, null=True)  # Field name made lowercase.
    nbbikes380 = models.IntegerField(db_column='nbBikes380', blank=True, null=True)  # Field name made lowercase.
    nbbikes384 = models.IntegerField(db_column='nbBikes384', blank=True, null=True)  # Field name made lowercase.
    nbbikes388 = models.IntegerField(db_column='nbBikes388', blank=True, null=True)  # Field name made lowercase.
    nbbikes392 = models.IntegerField(db_column='nbBikes392', blank=True, null=True)  # Field name made lowercase.
    nbbikes396 = models.IntegerField(db_column='nbBikes396', blank=True, null=True)  # Field name made lowercase.
    nbbikes404 = models.IntegerField(db_column='nbBikes404', blank=True, null=True)  # Field name made lowercase.
    nbbikes408 = models.IntegerField(db_column='nbBikes408', blank=True, null=True)  # Field name made lowercase.
    nbbikes416 = models.IntegerField(db_column='nbBikes416', blank=True, null=True)  # Field name made lowercase.
    nbbikes424 = models.IntegerField(db_column='nbBikes424', blank=True, null=True)  # Field name made lowercase.
    nbbikes428 = models.IntegerField(db_column='nbBikes428', blank=True, null=True)  # Field name made lowercase.
    nbbikes432 = models.IntegerField(db_column='nbBikes432', blank=True, null=True)  # Field name made lowercase.
    nbbikes440 = models.IntegerField(db_column='nbBikes440', blank=True, null=True)  # Field name made lowercase.
    nbbikes444 = models.IntegerField(db_column='nbBikes444', blank=True, null=True)  # Field name made lowercase.
    nbbikes448 = models.IntegerField(db_column='nbBikes448', blank=True, null=True)  # Field name made lowercase.
    nbbikes452 = models.IntegerField(db_column='nbBikes452', blank=True, null=True)  # Field name made lowercase.
    nbbikes456 = models.IntegerField(db_column='nbBikes456', blank=True, null=True)  # Field name made lowercase.
    nbbikes460 = models.IntegerField(db_column='nbBikes460', blank=True, null=True)  # Field name made lowercase.
    nbbikes464 = models.IntegerField(db_column='nbBikes464', blank=True, null=True)  # Field name made lowercase.
    nbbikes468 = models.IntegerField(db_column='nbBikes468', blank=True, null=True)  # Field name made lowercase.
    nbbikes472 = models.IntegerField(db_column='nbBikes472', blank=True, null=True)  # Field name made lowercase.
    nbbikes476 = models.IntegerField(db_column='nbBikes476', blank=True, null=True)  # Field name made lowercase.
    nbbikes480 = models.IntegerField(db_column='nbBikes480', blank=True, null=True)  # Field name made lowercase.
    nbbikes484 = models.IntegerField(db_column='nbBikes484', blank=True, null=True)  # Field name made lowercase.
    nbbikes492 = models.IntegerField(db_column='nbBikes492', blank=True, null=True)  # Field name made lowercase.
    nbbikes496 = models.IntegerField(db_column='nbBikes496', blank=True, null=True)  # Field name made lowercase.
    nbbikes500 = models.IntegerField(db_column='nbBikes500', blank=True, null=True)  # Field name made lowercase.
    nbbikes504 = models.IntegerField(db_column='nbBikes504', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks4 = models.IntegerField(db_column='nbEmptyDocks4', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks8 = models.IntegerField(db_column='nbEmptyDocks8', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks12 = models.IntegerField(db_column='nbEmptyDocks12', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks16 = models.IntegerField(db_column='nbEmptyDocks16', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks20 = models.IntegerField(db_column='nbEmptyDocks20', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks24 = models.IntegerField(db_column='nbEmptyDocks24', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks28 = models.IntegerField(db_column='nbEmptyDocks28', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks32 = models.IntegerField(db_column='nbEmptyDocks32', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks36 = models.IntegerField(db_column='nbEmptyDocks36', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks40 = models.IntegerField(db_column='nbEmptyDocks40', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks48 = models.IntegerField(db_column='nbEmptyDocks48', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks52 = models.IntegerField(db_column='nbEmptyDocks52', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks56 = models.IntegerField(db_column='nbEmptyDocks56', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks60 = models.IntegerField(db_column='nbEmptyDocks60', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks64 = models.IntegerField(db_column='nbEmptyDocks64', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks68 = models.IntegerField(db_column='nbEmptyDocks68', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks72 = models.IntegerField(db_column='nbEmptyDocks72', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks76 = models.IntegerField(db_column='nbEmptyDocks76', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks80 = models.IntegerField(db_column='nbEmptyDocks80', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks84 = models.IntegerField(db_column='nbEmptyDocks84', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks88 = models.IntegerField(db_column='nbEmptyDocks88', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks92 = models.IntegerField(db_column='nbEmptyDocks92', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks96 = models.IntegerField(db_column='nbEmptyDocks96', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks100 = models.IntegerField(db_column='nbEmptyDocks100', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks104 = models.IntegerField(db_column='nbEmptyDocks104', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks108 = models.IntegerField(db_column='nbEmptyDocks108', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks112 = models.IntegerField(db_column='nbEmptyDocks112', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks116 = models.IntegerField(db_column='nbEmptyDocks116', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks120 = models.IntegerField(db_column='nbEmptyDocks120', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks124 = models.IntegerField(db_column='nbEmptyDocks124', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks128 = models.IntegerField(db_column='nbEmptyDocks128', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks132 = models.IntegerField(db_column='nbEmptyDocks132', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks136 = models.IntegerField(db_column='nbEmptyDocks136', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks140 = models.IntegerField(db_column='nbEmptyDocks140', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks144 = models.IntegerField(db_column='nbEmptyDocks144', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks148 = models.IntegerField(db_column='nbEmptyDocks148', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks152 = models.IntegerField(db_column='nbEmptyDocks152', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks156 = models.IntegerField(db_column='nbEmptyDocks156', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks160 = models.IntegerField(db_column='nbEmptyDocks160', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks164 = models.IntegerField(db_column='nbEmptyDocks164', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks168 = models.IntegerField(db_column='nbEmptyDocks168', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks176 = models.IntegerField(db_column='nbEmptyDocks176', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks180 = models.IntegerField(db_column='nbEmptyDocks180', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks184 = models.IntegerField(db_column='nbEmptyDocks184', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks188 = models.IntegerField(db_column='nbEmptyDocks188', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks192 = models.IntegerField(db_column='nbEmptyDocks192', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks196 = models.IntegerField(db_column='nbEmptyDocks196', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks200 = models.IntegerField(db_column='nbEmptyDocks200', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks204 = models.IntegerField(db_column='nbEmptyDocks204', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks208 = models.IntegerField(db_column='nbEmptyDocks208', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks212 = models.IntegerField(db_column='nbEmptyDocks212', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks216 = models.IntegerField(db_column='nbEmptyDocks216', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks220 = models.IntegerField(db_column='nbEmptyDocks220', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks224 = models.IntegerField(db_column='nbEmptyDocks224', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks228 = models.IntegerField(db_column='nbEmptyDocks228', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks232 = models.IntegerField(db_column='nbEmptyDocks232', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks236 = models.IntegerField(db_column='nbEmptyDocks236', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks244 = models.IntegerField(db_column='nbEmptyDocks244', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks248 = models.IntegerField(db_column='nbEmptyDocks248', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks256 = models.IntegerField(db_column='nbEmptyDocks256', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks260 = models.IntegerField(db_column='nbEmptyDocks260', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks264 = models.IntegerField(db_column='nbEmptyDocks264', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks268 = models.IntegerField(db_column='nbEmptyDocks268', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks272 = models.IntegerField(db_column='nbEmptyDocks272', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks276 = models.IntegerField(db_column='nbEmptyDocks276', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks280 = models.IntegerField(db_column='nbEmptyDocks280', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks284 = models.IntegerField(db_column='nbEmptyDocks284', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks288 = models.IntegerField(db_column='nbEmptyDocks288', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks292 = models.IntegerField(db_column='nbEmptyDocks292', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks304 = models.IntegerField(db_column='nbEmptyDocks304', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks308 = models.IntegerField(db_column='nbEmptyDocks308', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks312 = models.IntegerField(db_column='nbEmptyDocks312', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks316 = models.IntegerField(db_column='nbEmptyDocks316', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks320 = models.IntegerField(db_column='nbEmptyDocks320', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks324 = models.IntegerField(db_column='nbEmptyDocks324', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks328 = models.IntegerField(db_column='nbEmptyDocks328', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks332 = models.IntegerField(db_column='nbEmptyDocks332', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks336 = models.IntegerField(db_column='nbEmptyDocks336', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks340 = models.IntegerField(db_column='nbEmptyDocks340', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks344 = models.IntegerField(db_column='nbEmptyDocks344', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks348 = models.IntegerField(db_column='nbEmptyDocks348', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks356 = models.IntegerField(db_column='nbEmptyDocks356', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks360 = models.IntegerField(db_column='nbEmptyDocks360', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks364 = models.IntegerField(db_column='nbEmptyDocks364', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks368 = models.IntegerField(db_column='nbEmptyDocks368', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks372 = models.IntegerField(db_column='nbEmptyDocks372', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks376 = models.IntegerField(db_column='nbEmptyDocks376', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks380 = models.IntegerField(db_column='nbEmptyDocks380', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks384 = models.IntegerField(db_column='nbEmptyDocks384', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks388 = models.IntegerField(db_column='nbEmptyDocks388', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks392 = models.IntegerField(db_column='nbEmptyDocks392', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks396 = models.IntegerField(db_column='nbEmptyDocks396', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks404 = models.IntegerField(db_column='nbEmptyDocks404', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks408 = models.IntegerField(db_column='nbEmptyDocks408', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks416 = models.IntegerField(db_column='nbEmptyDocks416', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks424 = models.IntegerField(db_column='nbEmptyDocks424', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks428 = models.IntegerField(db_column='nbEmptyDocks428', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks432 = models.IntegerField(db_column='nbEmptyDocks432', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks440 = models.IntegerField(db_column='nbEmptyDocks440', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks444 = models.IntegerField(db_column='nbEmptyDocks444', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks448 = models.IntegerField(db_column='nbEmptyDocks448', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks452 = models.IntegerField(db_column='nbEmptyDocks452', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks456 = models.IntegerField(db_column='nbEmptyDocks456', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks460 = models.IntegerField(db_column='nbEmptyDocks460', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks464 = models.IntegerField(db_column='nbEmptyDocks464', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks468 = models.IntegerField(db_column='nbEmptyDocks468', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks472 = models.IntegerField(db_column='nbEmptyDocks472', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks476 = models.IntegerField(db_column='nbEmptyDocks476', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks480 = models.IntegerField(db_column='nbEmptyDocks480', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks484 = models.IntegerField(db_column='nbEmptyDocks484', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks492 = models.IntegerField(db_column='nbEmptyDocks492', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks496 = models.IntegerField(db_column='nbEmptyDocks496', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks500 = models.IntegerField(db_column='nbEmptyDocks500', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks504 = models.IntegerField(db_column='nbEmptyDocks504', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True, blank=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'y_data_hourly'


class YDataHourlyWeb(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    month = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    hour = models.IntegerField(blank=True, null=True)
    nbbikes1 = models.IntegerField(db_column='nbBikes1', blank=True, null=True)  # Field name made lowercase.
    nbbikes5 = models.IntegerField(db_column='nbBikes5', blank=True, null=True)  # Field name made lowercase.
    nbbikes9 = models.IntegerField(db_column='nbBikes9', blank=True, null=True)  # Field name made lowercase.
    nbbikes13 = models.IntegerField(db_column='nbBikes13', blank=True, null=True)  # Field name made lowercase.
    nbbikes18 = models.IntegerField(db_column='nbBikes18', blank=True, null=True)  # Field name made lowercase.
    nbbikes22 = models.IntegerField(db_column='nbBikes22', blank=True, null=True)  # Field name made lowercase.
    nbbikes26 = models.IntegerField(db_column='nbBikes26', blank=True, null=True)  # Field name made lowercase.
    nbbikes32 = models.IntegerField(db_column='nbBikes32', blank=True, null=True)  # Field name made lowercase.
    nbbikes36 = models.IntegerField(db_column='nbBikes36', blank=True, null=True)  # Field name made lowercase.
    nbbikes40 = models.IntegerField(db_column='nbBikes40', blank=True, null=True)  # Field name made lowercase.
    nbbikes45 = models.IntegerField(db_column='nbBikes45', blank=True, null=True)  # Field name made lowercase.
    nbbikes49 = models.IntegerField(db_column='nbBikes49', blank=True, null=True)  # Field name made lowercase.
    nbbikes55 = models.IntegerField(db_column='nbBikes55', blank=True, null=True)  # Field name made lowercase.
    nbbikes60 = models.IntegerField(db_column='nbBikes60', blank=True, null=True)  # Field name made lowercase.
    nbbikes64 = models.IntegerField(db_column='nbBikes64', blank=True, null=True)  # Field name made lowercase.
    nbbikes69 = models.IntegerField(db_column='nbBikes69', blank=True, null=True)  # Field name made lowercase.
    nbbikes74 = models.IntegerField(db_column='nbBikes74', blank=True, null=True)  # Field name made lowercase.
    nbbikes78 = models.IntegerField(db_column='nbBikes78', blank=True, null=True)  # Field name made lowercase.
    nbbikes82 = models.IntegerField(db_column='nbBikes82', blank=True, null=True)  # Field name made lowercase.
    nbbikes86 = models.IntegerField(db_column='nbBikes86', blank=True, null=True)  # Field name made lowercase.
    nbbikes90 = models.IntegerField(db_column='nbBikes90', blank=True, null=True)  # Field name made lowercase.
    nbbikes94 = models.IntegerField(db_column='nbBikes94', blank=True, null=True)  # Field name made lowercase.
    nbbikes98 = models.IntegerField(db_column='nbBikes98', blank=True, null=True)  # Field name made lowercase.
    nbbikes102 = models.IntegerField(db_column='nbBikes102', blank=True, null=True)  # Field name made lowercase.
    nbbikes106 = models.IntegerField(db_column='nbBikes106', blank=True, null=True)  # Field name made lowercase.
    nbbikes110 = models.IntegerField(db_column='nbBikes110', blank=True, null=True)  # Field name made lowercase.
    nbbikes115 = models.IntegerField(db_column='nbBikes115', blank=True, null=True)  # Field name made lowercase.
    nbbikes119 = models.IntegerField(db_column='nbBikes119', blank=True, null=True)  # Field name made lowercase.
    nbbikes123 = models.IntegerField(db_column='nbBikes123', blank=True, null=True)  # Field name made lowercase.
    nbbikes127 = models.IntegerField(db_column='nbBikes127', blank=True, null=True)  # Field name made lowercase.
    nbbikes131 = models.IntegerField(db_column='nbBikes131', blank=True, null=True)  # Field name made lowercase.
    nbbikes135 = models.IntegerField(db_column='nbBikes135', blank=True, null=True)  # Field name made lowercase.
    nbbikes139 = models.IntegerField(db_column='nbBikes139', blank=True, null=True)  # Field name made lowercase.
    nbbikes143 = models.IntegerField(db_column='nbBikes143', blank=True, null=True)  # Field name made lowercase.
    nbbikes147 = models.IntegerField(db_column='nbBikes147', blank=True, null=True)  # Field name made lowercase.
    nbbikes151 = models.IntegerField(db_column='nbBikes151', blank=True, null=True)  # Field name made lowercase.
    nbbikes155 = models.IntegerField(db_column='nbBikes155', blank=True, null=True)  # Field name made lowercase.
    nbbikes159 = models.IntegerField(db_column='nbBikes159', blank=True, null=True)  # Field name made lowercase.
    nbbikes163 = models.IntegerField(db_column='nbBikes163', blank=True, null=True)  # Field name made lowercase.
    nbbikes167 = models.IntegerField(db_column='nbBikes167', blank=True, null=True)  # Field name made lowercase.
    nbbikes171 = models.IntegerField(db_column='nbBikes171', blank=True, null=True)  # Field name made lowercase.
    nbbikes176 = models.IntegerField(db_column='nbBikes176', blank=True, null=True)  # Field name made lowercase.
    nbbikes180 = models.IntegerField(db_column='nbBikes180', blank=True, null=True)  # Field name made lowercase.
    nbbikes184 = models.IntegerField(db_column='nbBikes184', blank=True, null=True)  # Field name made lowercase.
    nbbikes188 = models.IntegerField(db_column='nbBikes188', blank=True, null=True)  # Field name made lowercase.
    nbbikes192 = models.IntegerField(db_column='nbBikes192', blank=True, null=True)  # Field name made lowercase.
    nbbikes196 = models.IntegerField(db_column='nbBikes196', blank=True, null=True)  # Field name made lowercase.
    nbbikes200 = models.IntegerField(db_column='nbBikes200', blank=True, null=True)  # Field name made lowercase.
    nbbikes204 = models.IntegerField(db_column='nbBikes204', blank=True, null=True)  # Field name made lowercase.
    nbbikes208 = models.IntegerField(db_column='nbBikes208', blank=True, null=True)  # Field name made lowercase.
    nbbikes212 = models.IntegerField(db_column='nbBikes212', blank=True, null=True)  # Field name made lowercase.
    nbbikes216 = models.IntegerField(db_column='nbBikes216', blank=True, null=True)  # Field name made lowercase.
    nbbikes220 = models.IntegerField(db_column='nbBikes220', blank=True, null=True)  # Field name made lowercase.
    nbbikes224 = models.IntegerField(db_column='nbBikes224', blank=True, null=True)  # Field name made lowercase.
    nbbikes228 = models.IntegerField(db_column='nbBikes228', blank=True, null=True)  # Field name made lowercase.
    nbbikes233 = models.IntegerField(db_column='nbBikes233', blank=True, null=True)  # Field name made lowercase.
    nbbikes239 = models.IntegerField(db_column='nbBikes239', blank=True, null=True)  # Field name made lowercase.
    nbbikes244 = models.IntegerField(db_column='nbBikes244', blank=True, null=True)  # Field name made lowercase.
    nbbikes248 = models.IntegerField(db_column='nbBikes248', blank=True, null=True)  # Field name made lowercase.
    nbbikes253 = models.IntegerField(db_column='nbBikes253', blank=True, null=True)  # Field name made lowercase.
    nbbikes257 = models.IntegerField(db_column='nbBikes257', blank=True, null=True)  # Field name made lowercase.
    nbbikes261 = models.IntegerField(db_column='nbBikes261', blank=True, null=True)  # Field name made lowercase.
    nbbikes265 = models.IntegerField(db_column='nbBikes265', blank=True, null=True)  # Field name made lowercase.
    nbbikes269 = models.IntegerField(db_column='nbBikes269', blank=True, null=True)  # Field name made lowercase.
    nbbikes273 = models.IntegerField(db_column='nbBikes273', blank=True, null=True)  # Field name made lowercase.
    nbbikes277 = models.IntegerField(db_column='nbBikes277', blank=True, null=True)  # Field name made lowercase.
    nbbikes281 = models.IntegerField(db_column='nbBikes281', blank=True, null=True)  # Field name made lowercase.
    nbbikes285 = models.IntegerField(db_column='nbBikes285', blank=True, null=True)  # Field name made lowercase.
    nbbikes289 = models.IntegerField(db_column='nbBikes289', blank=True, null=True)  # Field name made lowercase.
    nbbikes293 = models.IntegerField(db_column='nbBikes293', blank=True, null=True)  # Field name made lowercase.
    nbbikes302 = models.IntegerField(db_column='nbBikes302', blank=True, null=True)  # Field name made lowercase.
    nbbikes306 = models.IntegerField(db_column='nbBikes306', blank=True, null=True)  # Field name made lowercase.
    nbbikes311 = models.IntegerField(db_column='nbBikes311', blank=True, null=True)  # Field name made lowercase.
    nbbikes315 = models.IntegerField(db_column='nbBikes315', blank=True, null=True)  # Field name made lowercase.
    nbbikes319 = models.IntegerField(db_column='nbBikes319', blank=True, null=True)  # Field name made lowercase.
    nbbikes323 = models.IntegerField(db_column='nbBikes323', blank=True, null=True)  # Field name made lowercase.
    nbbikes328 = models.IntegerField(db_column='nbBikes328', blank=True, null=True)  # Field name made lowercase.
    nbbikes332 = models.IntegerField(db_column='nbBikes332', blank=True, null=True)  # Field name made lowercase.
    nbbikes336 = models.IntegerField(db_column='nbBikes336', blank=True, null=True)  # Field name made lowercase.
    nbbikes340 = models.IntegerField(db_column='nbBikes340', blank=True, null=True)  # Field name made lowercase.
    nbbikes344 = models.IntegerField(db_column='nbBikes344', blank=True, null=True)  # Field name made lowercase.
    nbbikes348 = models.IntegerField(db_column='nbBikes348', blank=True, null=True)  # Field name made lowercase.
    nbbikes355 = models.IntegerField(db_column='nbBikes355', blank=True, null=True)  # Field name made lowercase.
    nbbikes359 = models.IntegerField(db_column='nbBikes359', blank=True, null=True)  # Field name made lowercase.
    nbbikes364 = models.IntegerField(db_column='nbBikes364', blank=True, null=True)  # Field name made lowercase.
    nbbikes368 = models.IntegerField(db_column='nbBikes368', blank=True, null=True)  # Field name made lowercase.
    nbbikes373 = models.IntegerField(db_column='nbBikes373', blank=True, null=True)  # Field name made lowercase.
    nbbikes377 = models.IntegerField(db_column='nbBikes377', blank=True, null=True)  # Field name made lowercase.
    nbbikes381 = models.IntegerField(db_column='nbBikes381', blank=True, null=True)  # Field name made lowercase.
    nbbikes387 = models.IntegerField(db_column='nbBikes387', blank=True, null=True)  # Field name made lowercase.
    nbbikes391 = models.IntegerField(db_column='nbBikes391', blank=True, null=True)  # Field name made lowercase.
    nbbikes396 = models.IntegerField(db_column='nbBikes396', blank=True, null=True)  # Field name made lowercase.
    nbbikes403 = models.IntegerField(db_column='nbBikes403', blank=True, null=True)  # Field name made lowercase.
    nbbikes408 = models.IntegerField(db_column='nbBikes408', blank=True, null=True)  # Field name made lowercase.
    nbbikes415 = models.IntegerField(db_column='nbBikes415', blank=True, null=True)  # Field name made lowercase.
    nbbikes419 = models.IntegerField(db_column='nbBikes419', blank=True, null=True)  # Field name made lowercase.
    nbbikes424 = models.IntegerField(db_column='nbBikes424', blank=True, null=True)  # Field name made lowercase.
    nbbikes428 = models.IntegerField(db_column='nbBikes428', blank=True, null=True)  # Field name made lowercase.
    nbbikes432 = models.IntegerField(db_column='nbBikes432', blank=True, null=True)  # Field name made lowercase.
    nbbikes439 = models.IntegerField(db_column='nbBikes439', blank=True, null=True)  # Field name made lowercase.
    nbbikes443 = models.IntegerField(db_column='nbBikes443', blank=True, null=True)  # Field name made lowercase.
    nbbikes447 = models.IntegerField(db_column='nbBikes447', blank=True, null=True)  # Field name made lowercase.
    nbbikes455 = models.IntegerField(db_column='nbBikes455', blank=True, null=True)  # Field name made lowercase.
    nbbikes459 = models.IntegerField(db_column='nbBikes459', blank=True, null=True)  # Field name made lowercase.
    nbbikes463 = models.IntegerField(db_column='nbBikes463', blank=True, null=True)  # Field name made lowercase.
    nbbikes467 = models.IntegerField(db_column='nbBikes467', blank=True, null=True)  # Field name made lowercase.
    nbbikes471 = models.IntegerField(db_column='nbBikes471', blank=True, null=True)  # Field name made lowercase.
    nbbikes475 = models.IntegerField(db_column='nbBikes475', blank=True, null=True)  # Field name made lowercase.
    nbbikes479 = models.IntegerField(db_column='nbBikes479', blank=True, null=True)  # Field name made lowercase.
    nbbikes483 = models.IntegerField(db_column='nbBikes483', blank=True, null=True)  # Field name made lowercase.
    nbbikes487 = models.IntegerField(db_column='nbBikes487', blank=True, null=True)  # Field name made lowercase.
    nbbikes492 = models.IntegerField(db_column='nbBikes492', blank=True, null=True)  # Field name made lowercase.
    nbbikes496 = models.IntegerField(db_column='nbBikes496', blank=True, null=True)  # Field name made lowercase.
    nbbikes500 = models.IntegerField(db_column='nbBikes500', blank=True, null=True)  # Field name made lowercase.
    nbbikes504 = models.IntegerField(db_column='nbBikes504', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks1 = models.IntegerField(db_column='nbEmptyDocks1', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks5 = models.IntegerField(db_column='nbEmptyDocks5', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks9 = models.IntegerField(db_column='nbEmptyDocks9', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks13 = models.IntegerField(db_column='nbEmptyDocks13', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks18 = models.IntegerField(db_column='nbEmptyDocks18', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks22 = models.IntegerField(db_column='nbEmptyDocks22', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks26 = models.IntegerField(db_column='nbEmptyDocks26', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks32 = models.IntegerField(db_column='nbEmptyDocks32', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks36 = models.IntegerField(db_column='nbEmptyDocks36', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks40 = models.IntegerField(db_column='nbEmptyDocks40', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks45 = models.IntegerField(db_column='nbEmptyDocks45', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks49 = models.IntegerField(db_column='nbEmptyDocks49', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks55 = models.IntegerField(db_column='nbEmptyDocks55', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks60 = models.IntegerField(db_column='nbEmptyDocks60', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks64 = models.IntegerField(db_column='nbEmptyDocks64', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks69 = models.IntegerField(db_column='nbEmptyDocks69', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks74 = models.IntegerField(db_column='nbEmptyDocks74', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks78 = models.IntegerField(db_column='nbEmptyDocks78', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks82 = models.IntegerField(db_column='nbEmptyDocks82', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks86 = models.IntegerField(db_column='nbEmptyDocks86', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks90 = models.IntegerField(db_column='nbEmptyDocks90', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks94 = models.IntegerField(db_column='nbEmptyDocks94', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks98 = models.IntegerField(db_column='nbEmptyDocks98', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks102 = models.IntegerField(db_column='nbEmptyDocks102', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks106 = models.IntegerField(db_column='nbEmptyDocks106', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks110 = models.IntegerField(db_column='nbEmptyDocks110', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks115 = models.IntegerField(db_column='nbEmptyDocks115', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks119 = models.IntegerField(db_column='nbEmptyDocks119', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks123 = models.IntegerField(db_column='nbEmptyDocks123', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks127 = models.IntegerField(db_column='nbEmptyDocks127', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks131 = models.IntegerField(db_column='nbEmptyDocks131', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks135 = models.IntegerField(db_column='nbEmptyDocks135', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks139 = models.IntegerField(db_column='nbEmptyDocks139', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks143 = models.IntegerField(db_column='nbEmptyDocks143', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks147 = models.IntegerField(db_column='nbEmptyDocks147', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks151 = models.IntegerField(db_column='nbEmptyDocks151', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks155 = models.IntegerField(db_column='nbEmptyDocks155', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks159 = models.IntegerField(db_column='nbEmptyDocks159', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks163 = models.IntegerField(db_column='nbEmptyDocks163', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks167 = models.IntegerField(db_column='nbEmptyDocks167', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks171 = models.IntegerField(db_column='nbEmptyDocks171', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks176 = models.IntegerField(db_column='nbEmptyDocks176', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks180 = models.IntegerField(db_column='nbEmptyDocks180', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks184 = models.IntegerField(db_column='nbEmptyDocks184', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks188 = models.IntegerField(db_column='nbEmptyDocks188', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks192 = models.IntegerField(db_column='nbEmptyDocks192', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks196 = models.IntegerField(db_column='nbEmptyDocks196', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks200 = models.IntegerField(db_column='nbEmptyDocks200', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks204 = models.IntegerField(db_column='nbEmptyDocks204', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks208 = models.IntegerField(db_column='nbEmptyDocks208', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks212 = models.IntegerField(db_column='nbEmptyDocks212', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks216 = models.IntegerField(db_column='nbEmptyDocks216', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks220 = models.IntegerField(db_column='nbEmptyDocks220', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks224 = models.IntegerField(db_column='nbEmptyDocks224', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks228 = models.IntegerField(db_column='nbEmptyDocks228', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks233 = models.IntegerField(db_column='nbEmptyDocks233', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks239 = models.IntegerField(db_column='nbEmptyDocks239', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks244 = models.IntegerField(db_column='nbEmptyDocks244', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks248 = models.IntegerField(db_column='nbEmptyDocks248', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks253 = models.IntegerField(db_column='nbEmptyDocks253', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks257 = models.IntegerField(db_column='nbEmptyDocks257', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks261 = models.IntegerField(db_column='nbEmptyDocks261', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks265 = models.IntegerField(db_column='nbEmptyDocks265', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks269 = models.IntegerField(db_column='nbEmptyDocks269', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks273 = models.IntegerField(db_column='nbEmptyDocks273', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks277 = models.IntegerField(db_column='nbEmptyDocks277', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks281 = models.IntegerField(db_column='nbEmptyDocks281', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks285 = models.IntegerField(db_column='nbEmptyDocks285', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks289 = models.IntegerField(db_column='nbEmptyDocks289', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks293 = models.IntegerField(db_column='nbEmptyDocks293', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks302 = models.IntegerField(db_column='nbEmptyDocks302', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks306 = models.IntegerField(db_column='nbEmptyDocks306', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks311 = models.IntegerField(db_column='nbEmptyDocks311', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks315 = models.IntegerField(db_column='nbEmptyDocks315', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks319 = models.IntegerField(db_column='nbEmptyDocks319', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks323 = models.IntegerField(db_column='nbEmptyDocks323', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks328 = models.IntegerField(db_column='nbEmptyDocks328', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks332 = models.IntegerField(db_column='nbEmptyDocks332', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks336 = models.IntegerField(db_column='nbEmptyDocks336', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks340 = models.IntegerField(db_column='nbEmptyDocks340', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks344 = models.IntegerField(db_column='nbEmptyDocks344', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks348 = models.IntegerField(db_column='nbEmptyDocks348', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks355 = models.IntegerField(db_column='nbEmptyDocks355', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks359 = models.IntegerField(db_column='nbEmptyDocks359', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks364 = models.IntegerField(db_column='nbEmptyDocks364', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks368 = models.IntegerField(db_column='nbEmptyDocks368', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks373 = models.IntegerField(db_column='nbEmptyDocks373', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks377 = models.IntegerField(db_column='nbEmptyDocks377', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks381 = models.IntegerField(db_column='nbEmptyDocks381', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks387 = models.IntegerField(db_column='nbEmptyDocks387', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks391 = models.IntegerField(db_column='nbEmptyDocks391', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks396 = models.IntegerField(db_column='nbEmptyDocks396', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks403 = models.IntegerField(db_column='nbEmptyDocks403', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks408 = models.IntegerField(db_column='nbEmptyDocks408', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks415 = models.IntegerField(db_column='nbEmptyDocks415', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks419 = models.IntegerField(db_column='nbEmptyDocks419', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks424 = models.IntegerField(db_column='nbEmptyDocks424', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks428 = models.IntegerField(db_column='nbEmptyDocks428', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks432 = models.IntegerField(db_column='nbEmptyDocks432', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks439 = models.IntegerField(db_column='nbEmptyDocks439', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks443 = models.IntegerField(db_column='nbEmptyDocks443', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks447 = models.IntegerField(db_column='nbEmptyDocks447', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks455 = models.IntegerField(db_column='nbEmptyDocks455', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks459 = models.IntegerField(db_column='nbEmptyDocks459', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks463 = models.IntegerField(db_column='nbEmptyDocks463', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks467 = models.IntegerField(db_column='nbEmptyDocks467', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks471 = models.IntegerField(db_column='nbEmptyDocks471', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks475 = models.IntegerField(db_column='nbEmptyDocks475', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks479 = models.IntegerField(db_column='nbEmptyDocks479', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks483 = models.IntegerField(db_column='nbEmptyDocks483', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks487 = models.IntegerField(db_column='nbEmptyDocks487', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks492 = models.IntegerField(db_column='nbEmptyDocks492', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks496 = models.IntegerField(db_column='nbEmptyDocks496', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks500 = models.IntegerField(db_column='nbEmptyDocks500', blank=True, null=True)  # Field name made lowercase.
    nbemptydocks504 = models.IntegerField(db_column='nbEmptyDocks504', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'y_data_hourly_web'
