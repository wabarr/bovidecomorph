from django.conf.urls import patterns, include, url
from bovidecoapp.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bovidecoapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'add_data/(?P<specimenID>\d+)', add_data),
    url(r'add_data/$', add_data),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', redirect2admin)
)
