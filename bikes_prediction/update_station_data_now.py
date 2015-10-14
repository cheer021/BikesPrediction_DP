import os
import django
from django.utils import timezone
import urllib
from lxml import etree
import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'bikes_prediction.settings'
django.setup()

from bikesmtl.models import Station, StationDataNow

dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')

root = etree.parse(dataNowMtl)
lastUpdate = datetime.datetime.utcfromtimestamp(int(int(root.xpath("//stations")[0].get("LastUpdate"))/1000))
lastUpdate = timezone.make_aware(lastUpdate)
for ele in root.xpath("//stations/station"):
	if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
		# station = StationDataNow(station = Station.objects.filter(station_id = int(ele.xpath("id")[0].text))[0], nb_bikes = int(ele.xpath("nbBikes")[0].text), nb_empty_docks = int(ele.xpath("nbEmptyDocks")[0].text), datetime = timezone.now(), last_comm_with_server = lastUpdate)
		# station.save()
		station = StationDataNow.objects.filter(station.station_id = int(ele.xpath("id")[0].text))
		station.nb_bikes = int(ele.xpath("nbBikes")[0].text)
		station.nb_empty_docks = int(ele.xpath("nbEmptyDocks")[0].text)
		station.datetime = timezone.now()
		station.last_comm_with_server = lastUpdate
