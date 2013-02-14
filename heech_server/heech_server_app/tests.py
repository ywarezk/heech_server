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
#from heech_server.heech_server_app.models import Drive


#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin testing
#===============================================================================

class ApiTest(ResourceTestCase):
    fixtures = ['users', 'apikey', 'heech_server_app']
    def setup(self):
        super(ApiTest, self).setup()
        
    def test_userprofile_auth(self):
        '''
        test that im the only one that can get my own profile
        '''
        #try to get the profile without password gives unauth
        resp = self.api_client.get('/api/v1/userprofile/1/', format='json')
        self.assertHttpUnauthorized(resp)
        
        #try to get yariv profile with ofir cradentials
        resp = self.api_client.get('/api/v1/userprofile/1/?username=ofir&api_key=12345678', format='json')
        self.assertHttpBadRequest(resp)
        
        #try to get yariv profile with yariv cradentials should work
        resp = self.api_client.get('/api/v1/userprofile/1/?username=yariv&api_key=12345678', format='json')
        self.assertValidJSONResponse(resp)
        
    
#    def test_usersettings_auth(self):
#        '''
#        check that on a settings other users cant put or get my settings and i can
#        '''
#        #try to get the setting of yariv without cradentials
#        resp = self.api_client.get('/api/v1/usersetting/1/', format='json')
#        self.assertHttpUnauthorized(resp)
#        
#        #try to get yariv settings with ofir cradentials
#        resp = self.api_client.get('/api/v1/usersetting/1/?username=ofir&api_key=12345678', format='json')
#        self.assertHttpBadRequest(resp)
#        
#        #try to put yariv settings with ofir cradentials
#        resp = self.api_client.put(uri='/api/v1/usersetting/1/?username=ofir&api_key=12345678', format='json', data={'search_radius': 1})
#        self.assertHttpBadRequest(resp)
#        
#        #yariv getting his settings should be ok
#        resp = self.api_client.get('/api/v1/usersetting/1/?username=yariv&api_key=12345678', format='json')
#        self.assertValidJSONResponse(resp)
#        
#        #yariv changing his setting should be ok
#        resp = self.api_client.put(uri='/api/v1/usersetting/1/?username=yariv&api_key=12345678', format='json', data={'search_radius': 1})
#        self.assertHttpAccepted(resp)
#        dictSetting = self.deserialize(resp)
#        self.assertEqual(dictSetting['search_radius'], 1)
#        
#    def test_drive_auth(self):
#        '''
#        check that others cant delete or modify my drive, i can post new one and get others
#        '''
#        #ofir cant delete or modify my drive
#        resp = self.api_client.delete(uri='/api/v1/drive/1/?username=ofir&api_key=12345678', format='json')
#        self.assertHttpBadRequest(resp)
#        resp = self.api_client.put(uri='/api/v1/drive/1/?username=ofir&api_key=12345678', format='json', data={'origin': 'fsdf'})
#        self.assertHttpBadRequest(resp)
#        
#        #ofir can get my drive
#        resp = self.api_client.get(uri='/api/v1/drive/1/?username=ofir&api_key=12345678', format='json')
#        self.assertValidJSONResponse(resp)
#        
#        #ofir can post a new drive
#        resp = self.api_client.post(uri='/api/v1/drive/?username=ofir&api_key=12345678', format='json', data={'origin': 'test1', 'destination': 'test2'})
#        print resp
#        self.assertHttpCreated(resp)
#        
#        #check put and delete for myself
#        resp = self.api_client.put(uri='/api/v1/drive/1/?username=yariv&api_key=12345678', format='json', data={'origin': 'sdf'})
#        self.assertHttpAccepted(resp)
#        resp = self.api_client.delete(uri='/api/v1/drive/1/?username=yariv&api_key=12345678', format='json')
#        self.assertHttpAccepted(resp)
#        self.assertEqual(Drive.objects.count(), 1)
        
        

#===============================================================================
# end testing
#===============================================================================