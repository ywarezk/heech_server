'''
Created on Jan 30, 2013
the rest api is defined here
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.resources import ModelResource
from heech_server_app.models import *
from heech_server.heech_server_app.models import UserProfile, University
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.exceptions import BadRequest
import json
#from tastypie import fields

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin constants
#===============================================================================

API_URL = '/api/v1/'

#===============================================================================
# end constants
#===============================================================================


#===============================================================================
# begin rest resources
#===============================================================================

class HeechAuthorization(DjangoAuthorization):
    '''
    authorization class objects with owner function only the owner can view them
    '''
    def is_authorized(self, request, obj=None):
        return super(DjangoAuthorization, self).is_authorized(request, obj)

    def apply_limits(self, request, object_list):
        if request == None:
            return object_list
        
        if request.method in ['POST']:
            return object_list
        
        objects = []
        for obj in object_list:
            if hasattr(obj, 'owner') and (obj.owner() == request.user.username):
                objects.append(obj)
        if len(objects) > 0:
            return objects
        else:
            raise BadRequest(json.dumps({'errors' : {'Authorization' : ('You are not authorized to modify this record',)}, }))

class NerdeezResource(ModelResource):
    '''
    abstract class with commone attribute common to all my rest models
    '''
    class Meta:
        authentication = ApiKeyAuthentication()
        authorization = HeechAuthorization()
        allowed_methods = ['get']
        always_return_data = True
        
    def obj_create(self, bundle, request=None, **kwargs):
        bundle.data['user_profile'] = API_URL + 'userprofile/' + str(request.user.get_profile().id) + '/'
        return super(NerdeezResource, self).obj_create(bundle, request, **kwargs)
        

class UserProfileResource(NerdeezResource):
    '''
    the rest api for the user profile model is defined here
    '''
    class Meta(NerdeezResource.Meta):
        queryset = UserProfile.objects.all()
        
class UniversityResource(NerdeezResource):
    '''
    the rest api for the  university resource
    '''
    class Meta(NerdeezResource.Meta):
        queryset = University.objects.all()
        allowed_methods = ['get', 'put', 'post']
        
#class UserSettingResource(NerdeezResource):
#    '''
#    the rest api for the user settings
#    '''
#    class Meta(NerdeezResource.Meta):
#        queryset = UserSetting.objects.all()
#        allowed_methods = ['get', 'put']
#        
#class DriveResource(NerdeezResource):
#    '''
#    the rest api for the users drives requests
#    '''
#    user_profile = fields.ToOneField(UserProfileResource, 'user_profile', full=True)
#    class Meta(NerdeezResource.Meta):
#        queryset = Drive.objects.all()
#        allowed_methods = ['get', 'put', 'post', 'delete']
#        
#    def apply_authorization_limits(self, request, object_list):
#        '''
#        only the owner can delete or update
#        '''
#        if request.method in ['PUT', 'DELETE']:
#            for drive in object_list:
#                if drive.user_profile.user.username != request.user.username:
#                    raise BadRequest(json.dumps({'errors' : {'Authorization' : ('You are not authorized to modify/delete this record',)}, }))
#                    return 
#        return object_list 

#===============================================================================
# end rest resources
#===============================================================================