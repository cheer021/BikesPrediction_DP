import json
from django.shortcuts import render
from django.http import *

from django.views.generic import View
from djangular.views.mixins import JSONResponseMixin

from .models import Station, StationDataNow

def index(request):
	return render(request, 'index.html')

class MyResponseView(JSONResponseMixin, View):
    def get_all_data(self):
        all_stations = StationDataNow.objects.all()
        data_list = []
        for s in all_stations:
        	data_list.append({'id': s.station.station_id, 
        		'name': s.station.name,
        		'nbBikes': s.nb_bikes,
        		'nbEmptyDocks': s.nb_empty_docks,
        		'lastCommWithServer': str(s.last_comm_with_server)})
		output = {'mtlData': data_list}
		return output
	
	def get_other_data(self):
		return ['baz', 'cap']

# def allStations(request):
	# all_stations = StationDataNow.objects.all()
	# data_list = []
	# for s in all_stations:
	# 	data_list.append({'id': s.station.station_id, 
	# 	'name': s.station.name,
	# 	'nbBikes': s.nb_bikes,
	# 	'nbEmptyDocks': s.nb_empty_docks,
	# 	'lastCommWithServer': str(s.last_comm_with_server)})
	# output = json.dumps({'mtlData': data_list})
# 	output = json.dumps({'mtlData': [{'id': 1, 
# 		'name': 'voula',
# 		'nbBikes': 5,
# 		'nbEmptyDocks': 5,
# 		'lastCommWithServer': 'now'}]})
# 	return HttpResponse(output, mimetype='application/javascript')

# def detail(request, station_id):
# 	try:
# 		s = StationDataNow.objects.get(station = Station.objects.get(station_id = int(station_id)))
# 	except Station.DoesNotExist:
# 		raise Http404("Station does not exist")
# 	return_obj = { 
# 		'name': s.station.name,
# 		'nbBikes': s.nb_bikes,
# 		'nbEmptyDocks': s.nb_empty_docks,
# 		'lastCommWithServer': str(s.last_comm_with_server)}
# 	context = {'station': return_obj}
# 	return render(request, 'detail.html', context)