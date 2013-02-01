from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'protocols.views.index', name='index'),
    url(r'^about$', 'protocols.views.about', name='about'),
    url(r'^(?P<protocol_id>\d+)/$', 'protocols.views.protocol_detail', name='protocol_detail'),
    url(r'^/new$', 'protocols.views.protocol_new', name='protocol_new'),
    url(r'^tags$', 'protocols.views.tag_list', name='tag_list'),
    url(r'^tags/(?P<tag_id>\d+)/$', 'protocols.views.tag_detail', name='tag_detail'),
    url(r'^users/(?P<user_id>\d+)/$', 'protocols.views.user_detail', name='user_detail'),
    url(r'^new_user$', 'protocols.views.user_new', name='user_new'),
    # url(r'^methods/', include('methods.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
