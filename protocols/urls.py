from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('protocols.views',
    url(r'^$', 'index'),
    url(r'index', 'index'),
    url(r'(?P<protocol_id>\d+)/$', 'detail'),
    url(r'^tags/(?P<tag_id>\d+)/$', 'tags'),
    url(r'^post/', 'add_protocol'),
    url(r'(?P<tag_name>\d+)/','tags'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
