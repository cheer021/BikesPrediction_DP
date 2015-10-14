import os
import django
from django.utils import timezone
import urllib
from lxml import etree

os.environ['DJANGO_SETTINGS_MODULE'] = 'bikes_prediction.settings'
django.setup()

from bikesmtl.models import Station

Station.objects.all().delete()

dataNowMtl = urllib.urlopen('http://montreal.bixi.com/data/bikeStations.xml')

root = etree.parse(dataNowMtl)
for ele in root.xpath("//stations/station"):
	if ele.xpath("installed")[0].text == "true" and ele.xpath("locked")[0].text == "false":
		s = Station(station_id = int(ele.xpath("id")[0].text), name = ele.xpath("name")[0].text, latitude = float(ele.xpath("lat")[0].text), longitude = float(ele.xpath("long")[0].text))
		s.save()