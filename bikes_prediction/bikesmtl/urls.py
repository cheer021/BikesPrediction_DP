from django.conf.urls import patterns, include, url
from . import views
# from .api import MyCRUDView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^bikesmtl/stations/all/info$', views.MyResponseView.as_view(), {'invoke_method': 'get_all_station_info'}),
	url(r'^bikesmtl/stations/(?P<station_id>[0-9]+)/info$', views.MyResponseView.as_view(), {'invoke_method': 'get_station_info'}),
	url(r'^bikesmtl/stations/all/now$', views.MyResponseView.as_view(), {'invoke_method': 'get_all_data_now'}),
	url(r'^bikesmtl/stations/(?P<station_id>[0-9]+)/now$', views.MyResponseView.as_view(), {'invoke_method': 'get_station_data_now'}),
	url(r'^bikesmtl/stations/all/predictions$', views.MyResponseView.as_view(), {'invoke_method': 'get_all_predictions'}),
	url(r'^bikesmtl/stations/(?P<station_id>[0-9]+)/predictions$', views.MyResponseView.as_view(), {'invoke_method': 'get_station_predictions'}),
)
