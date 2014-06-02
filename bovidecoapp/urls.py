from django.conf.urls import patterns, include, url
from django.contrib import admin

from bovidecoapp.views import *


admin.autodiscover()

#intitialize API
from tastypie.api import Api
from API.API_resources import MeasurementResource
v1_api = Api(api_name='v1')
v1_api.register(MeasurementResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bovidecoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^API/', include(v1_api.urls)),
    url(r'add_data/(?P<specimenID>\d+)', add_data),
    url(r'add_data/$', add_data),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', redirect2admin)
)
