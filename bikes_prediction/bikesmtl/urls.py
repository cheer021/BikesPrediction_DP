from django.conf.urls import patterns, include, url
from . import views
# from .api import MyCRUDView

urlpatterns = patterns('',
	url(r'^index', views.index, name='index'),
	url(r'^$', views.mapView, name='mapView'),
	url(r'^map', views.mapView, name='mapView'),
	url(r'^list', views.listView, name='listView'),
	url(r'^bikesmtl/stations/all/info$', views.MyResponseView.as_view(), {'invoke_method': 'get_all_station_info'}),
	url(r'^bikesmtl/stations/all/predictions/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<hour>[0-9]+)$', views.MyPredictionView.as_view(), {'invoke_method': 'get_all_predictions'}, name='get-predictions'),
	url(r'^bikesmtl/stations/all/actual/(?P<month>[0-9]+)/(?P<day>[0-9]+)/(?P<hour>[0-9]+)$', views.MyActualView.as_view(), {'invoke_method': 'get_all_actual'}, name='get-actual'),
	# url(r'^bikesmtl/stations/all/predictions', views.predictionView, name='get-predictions'),
	# url(r'^bikesmtl/stations/all/actual$', views.actualView, name='actualView'),

)
