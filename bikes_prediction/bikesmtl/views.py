import json
import sqlite3
# import os

from django.shortcuts import render
from django.http import *
from django.views.generic import View, DetailView
from django.views.generic.detail import BaseDetailView
from djangular.views.mixins import JSONResponseMixin
from django.contrib.staticfiles.views import serve
import csv
from django.http import HttpResponse
# from django.core.urlresolvers import reverse

from .models import BikesmtlStation, YDataHourlyWeb, PredictedDataHourly #, DataHourly

def index(request):
	return render(request, 'index.html')

def mapView(request):
	return render(request, 'mapView.html')

def listView(request):
	return render(request, 'listView.html')

# def actualView(request):
# 	response = HttpResponse(content_type='text/csv')
# 	response['Content-Disposition'] = 'attachment; filename="y_actual.csv"'
# 	writer = csv.writer(response)
# 	with open('y_predicted.csv', 'rb') as f:
#     	reader = csv.reader(f)
# 		for r in reader:
# 			writer.writerow(r)
# 	return response

# class JSONResponseMixin(object):
#     def render_to_response(self, context):
#         "Returns a JSON response containing 'context' as payload"
#         return self.get_json_response(self.convert_context_to_json(context))

#     def get_json_response(self, content, **httpresponse_kwargs):
#         "Construct an `HttpResponse` object."
#         return http.HttpResponse(content,
#                                  content_type='application/json',
#                                  **httpresponse_kwargs)

#     def convert_context_to_json(self, context):
#         "Convert the context dictionary into a JSON object"
#         # Note: This is *EXTREMELY* naive; in reality, you'll need
#         # to do much more complex handling to ensure that arbitrary
#         # objects -- such as Django model instances or querysets
#         # -- can be serialized as JSON.
#         return json.dumps(context)

class MyResponseView(JSONResponseMixin, View):
	
	def get_all_station_info(self):
		all_stations = BikesmtlStation.objects.all()
		data_list = []
		for s in all_stations:
			data_list.append({'id': s.station, 
				'name': s.name, 
				'latitude': s.latitude, 
				'longitude': s.longitude})
		output = {'mtlData': data_list}
		return output

class MyPredictionView(JSONResponseMixin, BaseDetailView):

	model = PredictedDataHourly

	# def render_to_response(self, context, **response_kwargs):
 #        return self.render_to_json_response(context, **response_kwargs)

	def get_all_predictions(self):
		# m = self.args['month']
		# d = self.args.day
		# h = self.args.hour
		m=4
		d=23
		h=0
		data_list = []
		row = PredictedDataHourly.objects.get(month=m, day=d, hour=h)
		stations = BikesmtlStation.objects.all()
		fields = PredictedDataHourly._meta.get_all_field_names()
		fields.sort()
		fields = fields[4:]
		fields = fields[:len(fields)/2]
		station_fields = [int(float(f[7:])) for f in fields]
		station_fields.sort()
		for s, station in enumerate(stations):
			if s%4==0 and s in station_fields:
				# data_list.append(getattr(row, 'nbbikes'+str(i)))
				data_list.append({'id': station.station, 
					'nbBikes': getattr(row, 'nbbikes'+str(s)), 
					'nbEmptyDocks': getattr(row, 'nbemptydocks'+str(s))})
		
		output = {'mtlData': data_list}
		return output

class MyActualView(JSONResponseMixin, DetailView):

	model = YDataHourlyWeb

	# def render_to_response(self, context):
 #        return JSONResponseMixin.render_to_response(self, context)

	def get_all_actual(self):
		# month = self.args.month
		# day = self.args.day
		# hour = self.args.hour
		month = 4
		day = 23
		hour = 0
		data_list = []
		row = YDataHourlyWeb.objects.get(month=month, day=day, hour=hour)
		stations = BikesmtlStation.objects.all()
		fields = YDataHourlyWeb._meta.get_all_field_names()
		fields.sort()
		fields = fields[4:]
		fields = fields[:len(fields)/2]
		station_fields = [int(float(f[7:])) for f in fields]
		station_fields.sort()
		for s, station in enumerate(stations):
			if s in station_fields:
				# continue
				# data_list.append(getattr(row, 'nbbikes'+str(i)))
				data_list.append({'id': station.station, 
					'nbBikes': getattr(row, 'nbbikes'+str(s)), 
					'nbEmptyDocks': getattr(row, 'nbemptydocks'+str(s))})

		output = {'mtlData': data_list}
		return output

