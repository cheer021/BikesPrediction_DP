import json
from django.shortcuts import render
from django.http import *

from django.views.generic import View
from djangular.views.mixins import JSONResponseMixin

from .models import Station, StationDataNow, StationDataPredictions

def index(request):
	return render(request, 'index.html')

class MyResponseView(JSONResponseMixin, View):
	def get_all_station_info(self):
		all_stations = Station.objects.all()
		data_list = []
		for s in all_stations:
			data_list.append({'id': s.station_id, 
				'name': s.name, 
				'latitude': s.latitude, 
				'longitude': str(s.longitude)})
		output = {'mtlData': data_list}
		return output
	def get_station_info(self, station_id):
		station = Station.objects.get(station_id = station_id)
		data = {'id': station_id, 
			'name': station.name, 
			'latitude': station.latitude, 
			'longitude': str(station.longitude)}
		return data

	def get_all_data_now(self):
		all_stations = StationDataNow.objects.all()
		data_list = []
		for s in all_stations:
			data_list.append({'id': s.station.station_id, 
				'nbBikes': s.nb_bikes, 
				'nbEmptyDocks': s.nb_empty_docks, 
				'lastCommWithServer': str(s.last_comm_with_server)})
		output = {'mtlData': data_list}
		return output

	def get_station_data_now(self, station_id):
		station = Station.objects.get(station_id = station_id)
		stationData = StationDataNow.objects.get(station = station)
		data = {'id': station_id, 
			'nbBikes': stationData.nb_bikes, 
			'nbEmptyDocks': stationData.nb_empty_docks, 
			'lastCommWithServer': str(stationData.last_comm_with_server)}
		return data

	def get_all_predictions(self):
		all_stations = StationDataPredictions.objects.all()
		data_list = []
		for s in all_stations:
			data_list.append({'id': s.station.station_id, 
				'nbBikes5': s.nb_bikes_5, 
				'nbEmptyDocks5': s.nb_empty_docks_5, 
				'nbBikes10': s.nb_bikes_10, 
				'nbEmptyDocks10': s.nb_empty_docks_10, 
				'nbBikes15': s.nb_bikes_15, 
				'nbEmptyDocks15': s.nb_empty_docks_15, 
				'nbBikes30': s.nb_bikes_30, 
				'nbEmptyDocks30': s.nb_empty_docks_30, 
				'updatedAt': str(s.updated_at)})
		output = {'mtlData': data_list}
		return output

	def get_station_predictions(self, station_id):
		station = Station.objects.get(station_id = station_id)
		stationData = StationDataPredictions.objects.get(station = station)
		data = {'id': station_id, 
			'nbBikes5': stationData.nb_bikes_5, 
			'nbEmptyDocks5': stationData.nb_empty_docks_5, 
			'nbBikes10': stationData.nb_bikes_10, 
			'nbEmptyDocks10': stationData.nb_empty_docks_10, 
			'nbBikes15': stationData.nb_bikes_15, 
			'nbEmptyDocks15': stationData.nb_empty_docks_15, 
			'nbBikes30': stationData.nb_bikes_30, 
			'nbEmptyDocks30': stationData.nb_empty_docks_30, 
			'updatedAt': str(stationData.updated_at)}
		return data
