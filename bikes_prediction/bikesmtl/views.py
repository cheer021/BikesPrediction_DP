import json
import sqlite3

from django.shortcuts import render
from django.http import *
from django.views.generic import View
from djangular.views.mixins import JSONResponseMixin

def index(request):
	return render(request, 'index.html')

def mapView(request):
	return render(request, 'mapView.html')

def listView(request):
	return render(request, 'listView.html')

class MyResponseView(JSONResponseMixin, View):
	
	def get_all_station_info(self):
		conn = sqlite3.connect('bikedb')
		c = conn.cursor()
		c.execute("select * from bikesmtl_station order by station")
		all_stations = c.fetchall()
		data_list = []
		for s in all_stations:
			data_list.append({'id': s[4], 
				'name': s[0], 
				'latitude': s[1], 
				'longitude': s[2]})
		output = {'mtlData': data_list}
		conn.close()
		return output

	def get_all_predictions(self, month, day, hour):
		conn = sqlite3.connect('bikedb')
		c = conn.cursor()
		c.execute("select * from predicted_data_hourly where month=? and day=? and hour=?", (month, day, hour))
		predictions = c.fetchone()[3:] #remove month,day,hour from result
		bikes = predictions[:len(predictions)/2]
		docks = predictions[len(predictions)/2:]
		c.execute("select station from bikesmtl_station order by station")
		all_stations = list(sum(c.fetchall(), ()))
		data_list = []
		for i,s in enumerate(all_stations):
			data_list.append({'id': s, 
				'nbBikes': bikes[i], 
				'nbEmptyDocks': docks[i]})
		output = {'mtlData': data_list}
		conn.close()
		return output

	def get_all_actual(self, month, day, hour):
		conn = sqlite3.connect('bikedb')
		c = conn.cursor()
		c.execute("select * from y_data_hourly where month=? and day=? and hour=?", (month, day, hour))
		actual = c.fetchone()[3:] #remove month,day,hour from result
		bikes = actual[:len(actual)/2]
		docks = actual[len(actual)/2:]
		c.execute("select station from bikesmtl_station order by station")
		all_stations = list(sum(c.fetchall(), ()))
		data_list = []
		for i,s in enumerate(all_stations):
			data_list.append({'id': s, 
				'nbBikes': bikes[i], 
				'nbEmptyDocks': docks[i]})
		output = {'mtlData': data_list}
		conn.close()
		return output

