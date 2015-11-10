# from django.core.management.base import BaseCommand
from bikesmtl.models import Station, StationDataNow, StationDataPredictions
from django.utils import timezone
import datetime
import urllib
from lxml import etree

from django_cron import CronJobBase, Schedule

class UpdateStationDataNow(CronJobBase):
    RUN_EVERY_MINS = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'bikesmtl.update_station_data_now'    # a unique code

    def do(self):
        dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')
        root = etree.parse(dataNowMtl)

        lastUpdate = datetime.datetime.utcfromtimestamp(int(int(root.xpath("//stations")[0].get("LastUpdate"))/1000))
        lastUpdate = timezone.make_aware(lastUpdate)
        for ele in root.xpath("//stations/station"):
            if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
                try:
                    station = StationDataNow.objects.get(station = Station.objects.get(station_id = int(ele.xpath("id")[0].text)))
                    station.nb_bikes = int(ele.xpath("nbBikes")[0].text)
                    station.nb_empty_docks = int(ele.xpath("nbEmptyDocks")[0].text)
                    station.updated_at = timezone.now()
                    station.last_comm_with_server = lastUpdate
                except ObjectDoesNotExist:
                    s = StationDataNow(station = Station.objects.get(station_id = int(ele.xpath("id")[0].text)), nb_bikes = ele.xpath("nbBikes")[0].text, nb_empty_docks = float(ele.xpath("nbEmptyDocks")[0].text), updated_at = timezone.now(), last_comm_with_server = lastUpdate)
                    s.save()
        self.stdout.write("Updated Station Data at " + timezone.now())
                          

class UpdateStationInfo(CronJobBase):
    RUN_AT_TIMES = ['4:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'bikesmtl.update_station_data_now'    # a unique code

    def do(self):
        dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')
        root = etree.parse(dataNowMtl)

        for ele in root.xpath("//stations/station"):
            if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
                try:
                    s = Station.objects.get(station_id = int(ele.xpath("id")[0].text))
                    s.name = ele.xpath("name")[0].text
                    s.latitude = float(ele.xpath("lat")[0].text)
                    s.longitude = float(ele.xpath("long")[0].text)
                except ObjectDoesNotExist:
                    s = Station(station_id = int(ele.xpath("id")[0].text), name = ele.xpath("name")[0].text, latitude = float(ele.xpath("lat")[0].text), longitude = float(ele.xpath("long")[0].text))
                    s.save()
            else:
                try:
                    s = Station.objects.get(station_id = int(ele.xpath("id")[0].text))
                    s.delete()
                except ObjectDoesNotExist:
                    continue  
        self.stdout.write("Updated Station Info at " + timezone.now())           
