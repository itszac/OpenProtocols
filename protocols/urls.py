from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'protocols.views.index', name='index'),
    url(r'^logout$', 'protocols.views.logout_view', name='logout'),
    url(r'^login$', 'protocols.views.login_view', name='login'),
    url(r'^(?P<protocol_id>\d+)/$', 'protocols.views.protocol_detail', name='protocol_detail'),
    url(r'^new$', 'protocols.views.protocol_new', name='protocol_new'),
    url(r'^tags$', 'protocols.views.tag_list', name='tag_list'),
    url(r'^tags/(?P<tag_name>\w+)/$', 'protocols.views.tag_detail', name='tag_detail'),
    url(r'^users/(?P<user_id>\d+)/$', 'protocols.views.user_detail', name='user_detail'),
    url(r'^new_user$', 'protocols.views.user_new', name='user_new'),
    url(r'^vote/(?P<document_id>\d+)/$', 'protocols.views.vote', name='tag_detail'),
    url(r'^tag/(?P<document_id>\d+)/$', 'protocols.views.add_tag', name='add_tag'),
    url(r'^comment/(?P<document_id>\d+)/$', 'protocols.views.add_comment', name='add_comment'),
    # url(r'^methods/', include('methods.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
