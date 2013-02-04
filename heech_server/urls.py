#===============================================================================
# import statments
#===============================================================================

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from heech_server.heech_server_app.heech_api.api import UserProfileResource, UserSettingResource, DriveResource
from tastypie.api import Api
import heech_server_app.views

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin url definition
#===============================================================================

#enable admin
admin.autodiscover()

#register for tastypie api
v1_api = Api(api_name='v1')
v1_api.register(UserProfileResource())
v1_api.register(UserSettingResource())
v1_api.register(DriveResource())

#url define
urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^grappelli/', include('grappelli.urls')),
     (r'^api/', include(v1_api.urls)),
      (r'^$', heech_server_app.views.test),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

#===============================================================================
# end url definition
#===============================================================================


