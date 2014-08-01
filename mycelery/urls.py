from django.conf.urls import patterns, include, url

from django.contrib import admin
from demoapp.views import see_view
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^myview/', 'demoapp.views.see_view'),
    url(r'^admin/', include(admin.site.urls)),
)
