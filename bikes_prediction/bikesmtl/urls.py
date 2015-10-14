# from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from bikes_prediction import settings

from . import views

# admin.autodiscover()

# urlpatterns = patterns(
#     '',
#     url('^.*$', views.IndexView.as_view(), name='index'),
# ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()

# urlpatterns += [
# 	url(r'^bikedatanow/', include('bikesmtl.urls', namespace="bikesmtl")),
#     url(r'^admin/', include(admin.site.urls)),
# ]

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<station_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^admin/', include(admin.site.urls)),
]