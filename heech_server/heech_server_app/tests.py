'''
Created on Jan 30, 2013
test file for my rest api
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.test import ResourceTestCase

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin testing
#===============================================================================

class ApiTest(ResourceTestCase):
    def setup(self):
        super(ApiTest, self).setup()
        
    def test_userprofile_auth(self):
        '''
        test that im the only one that can get my own profile
        '''
        pass
    
    def test_usersettings_auth(self):
        '''
        check that on a settings other users cant put or get my settings and i can
        '''
        pass
        
    def test_drive_auth(self):
        '''
        check that others cant delete or modify my drive, i can post new one and get others
        '''
        pass
        

#===============================================================================
# end testing
#===============================================================================