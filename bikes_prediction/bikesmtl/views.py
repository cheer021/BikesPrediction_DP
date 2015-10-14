# import json
from django.shortcuts import render

from .models import Station, StationDataNow

# def list(request, station_id=None):
# 	queryset = StationDataNow.objects.all().filter(station.station_id=station_id)
# 	data_list = []
# 	for s in queryset:
# 		data_list.append({'id': s.station.station_id, 
# 		'name': s.station.name,
# 		'nbBikes': s.nb_bikes,
# 		'nbEmptyDocks': s.nb_empty_docks,
# 		'lastCommWithServer': str(s.last_comm_with_server)})
# 	output = json.dumps({'mtlData': data_list})
# 	return output

# from django.views.decorators.csrf import ensure_csrf_cookie
# from django.views.generic.base import TemplateView
# from django.utils.decorators import method_decorator


# class IndexView(TemplateView):
#     template_name = 'index.html'

#     @method_decorator(ensure_csrf_cookie)
#     def dispatch(self, *args, **kwargs):
#         return super(IndexView, self).dispatch(*args, **kwargs)

def index(request):
	all_stations = StationDataNow.objects.all()
	# data_list = []
	# for s in all_stations:
	# 	data_list.append({'id': s.station.station_id, 
	# 	'name': s.station.name,
	# 	'nbBikes': s.nb_bikes,
	# 	'nbEmptyDocks': s.nb_empty_docks,
	# 	'lastCommWithServer': str(s.last_comm_with_server)})
	# output = json.dumps({'mtlData': data_list})
	# return output
	# template = loader.get_template('index.html')
	context = {'station_data_now_list': all_stations}
	return render(request, 'index.html', context)

def detail(request, station_id):
	try:
		s = StationDataNow.objects.get(station = Station.objects.get(station_id = int(station_id)))
	except Station.DoesNotExist:
		raise Http404("Station does not exist")
	return_obj = { 
		'name': s.station.name,
		'nbBikes': s.nb_bikes,
		'nbEmptyDocks': s.nb_empty_docks,
		'lastCommWithServer': str(s.last_comm_with_server)}
	context = {'station': return_obj}
	return render(request, 'detail.html', context)