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
from decimal import Decimal
from tastypie.models import create_api_key
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
        '''
        what will be printed in the admin
        '''
        return u'Profile of user: %s, name %s %s' % (self.user.username, self.first_name, self.last_name)
    
    def owner(self):
        '''
        security only owner can view settings
        '''
        return self.user.username
    
    
class UserSetting(NerdeezModel):
    '''
    this model will contain application setting for every user
    all new user will have a default settings
    '''
    search_radius_choices = (
                                 (0, 'Unlimited'),
                                 (1, 'My friends'),
                                 (2, 'Friends of friends'),
                            )
    user_profile = models.ForeignKey(UserProfile, unique=True)
    search_radius = models.IntegerField(default=0, choices=search_radius_choices)
    is_notify_similar_passenger = models.BooleanField(default=True) #im a driver - notify me when there is a passenger i can collect
    is_notify_similar_driver = models.BooleanField(default=True) # im a passenger notify me if there is a driver going to the same direction
    
    def __unicode__(self):
        '''
        what will be printed in the admin
        '''
        return u'%s %s Settings' %(self.user_profile.first_name, self.user_profile.last_name)
    
    def owner(self):
        '''
        security only owner can view settings
        '''
        return self.user_profile.user.username

    
class Drive(NerdeezModel):
    '''
    this model will save the users hitchiking needs
    '''
    user_profile = models.ForeignKey(UserProfile, unique=True)
    drive_date = models.DateTimeField(default=lambda: datetime.datetime.now().replace(microsecond=0))
    origin = models.CharField(max_length=100, blank=True, null=True , default="")
    destination = models.CharField(max_length=100, blank=True, null=True , default="")
    price = models.DecimalField(max_digits = 6, decimal_places = 3,default = Decimal("0.00"))
    
    def __unicode__(self):
        '''
        what will be printed in the admin
        '''
        return 'User: %s %s Wants to go from: %s to: %s' % (self.user_profile.first_name, 
                                                            self.user_profile.last_name, 
                                                            self.origin, 
                                                            self.destination)
        

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
models.signals.post_save.connect(create_api_key, sender=User)

#===============================================================================
# end signals
#===============================================================================