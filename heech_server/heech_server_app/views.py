'''
Created on Feb 2, 2013
will create the views for the server app
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from django.http import HttpResponse
#from tastypie.models import ApiKey
#from django.contrib.auth.models import User

#===============================================================================
# end imports
#===============================================================================

def test(request):
    '''
    view for testing stuff
    '''
    '''uYariv, created= User.objects.get_or_create(username='yariv', first_name='Yariv', last_name='Katz', email='yariv@purplebit.com')
    uOfir, created= User.objects.get_or_create(username='ofir', first_name='Ofir', last_name='Ovadia', email='ofir@purplebit.com')
    uYariv.set_password('housekitten4')
    uOfir.set_password('housekitten4')
    uYariv.save()
    uOfir.save()'''
    return HttpResponse('hello world')
