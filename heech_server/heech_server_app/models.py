'''
Created on Jan 28, 2013
contains the db models
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# imports
#===============================================================================
from django.db import models
import datetime
from django.contrib.auth.models import User
#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin heech models
#===============================================================================

class NerdeezModel(models.Model):
    '''
    this class will be an abstract class for all my models
    and it will contain common information
    '''
    creation_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0))
    modified_data = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0), auto_now=True)
    
    class Meta:
        abstract = True
        
class UserProfile(NerdeezModel):
    '''
    this model will contain the user account on heech
    it will save all the users data from facebook and will be saved on registration
    '''
    user = models.OneToOneField(User, unique=True, related_name='profile')
    facebook_id = models.CharField(max_length = 255, null = True, blank = True, default="")
    first_name = models.CharField(max_length=30, blank=True, null=True , default="")
    last_name = models.CharField(max_length=30, blank=True, null=True , default="")
    gender = models.CharField(max_length=10, blank=True, null=True , default="")
    facebook_username = models.CharField(max_length=50, blank=True, null=True , default="")
    facebook_link = models.CharField(max_length=200, blank=True, null=True , default="")
    
    def __unicode__(self):
        return u'Profile of user: %s, name %s %s' % (self.user.username, self.first_name, self.last_name)


#===============================================================================
# end heech models
#===============================================================================

#===============================================================================
# begin signals
#===============================================================================

#when creating user create also the userprofile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User, dispatch_uid="create_user_profile_on_user_create")


#===============================================================================
# end signals
#===============================================================================