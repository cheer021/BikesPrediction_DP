from django.conf.urls import patterns, include, url
from . import views
# from .api import MyCRUDView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# url(r'^bikesmtl/$', StationDataNowList.as_view(), name='station-data-now-list'),
	# url(r'^crud/bikesmtl/?$', MyCRUDView.as_view(), name='my_crud_view'),
	url(r'^bikesmtl$', views.MyResponseView.as_view(), {'invoke_method': 'get_all_data'}),
    # url(r'^fetch-other-data.json$', views.MyResponseView.as_view(), {'invoke_method': 'get_other_data'}),
	# url(r'^$', TemplateView.as_view(template_name='index.html')),
    # url(r'^(?P<station_id>[0-9]+)/$', views.detail, name='detail'),
)