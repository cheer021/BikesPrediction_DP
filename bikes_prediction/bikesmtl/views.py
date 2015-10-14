from django.shortcuts import render
from django.http import HttpResponse

from bikesmtl.models import StationDataNow

def index(request):
	all_stations = StationDataNow.objects.all()
	output = ', '.join([(s.station_id) for s in all_stations])
	return HttpResponse(output)

def detail(request, station_id):
    return HttpResponse("You're looking at station %s." % station_id)