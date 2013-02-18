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

from heech_server.heech_server_app.models import UserProfile
from django.contrib.auth.models import User

#===============================================================================
# end imports
#===============================================================================


def register(request):
    '''
    register a user to our system
    '''
    user = User(username='ywarezk')
    user.set_password('housekitten4')
    user.save()
