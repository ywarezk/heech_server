#===============================================================================
# import statments
#===============================================================================

from django.conf.urls import patterns, include, url
from django.conf import settings

#===============================================================================
# end imports
#===============================================================================

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heech_server.views.home', name='home'),
    # url(r'^heech_server/', include('heech_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^grappelli/', include('grappelli.urls')),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
