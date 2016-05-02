import requests
import base64
import json
import datetime as dt

PARTICLE_API_URL = 'https://api.particle.io'

AUTH_TOKEN_URL = PARTICLE_API_URL + '/oauth/token'
LIST_TOKENS_URL = PARTICLE_API_URL + '/v1/access_tokens' # Unimplemented
DEVICES_URL = PARTICLE_API_URL + '/v1/devices'

class Particle():

    # Initialise connection with Cloud API
    # 
    # If login details are provided a new access token will be generated otherwise the token given will be used.
    # The provided token is not checked for validity
    def __init__(self, username=None, password=None, access_token=None):
        
        if username is not None and password is not None:
            self.username = username
            self.password = password
        
            headers = {'Authorization': 'Basic %s' % base64.encodestring('particle:particle').replace('\n', '')}
            
            data = {
                'grant_type': 'password',
                'username': self.username,
                'password': self.password
            }
                
            try:      
                response_obj = self.api('POST', AUTH_TOKEN_URL, data=data, headers=headers)
            except:
                raise
    
            self.access_token = response_obj['access_token']
            self.access_token_expiry_date = dt.datetime.now() + dt.timedelta(seconds=response_obj['expires_in'])
            self.refresh_token = response_obj['refresh_token'] 
 
        elif access_token is not None:
            self.access_token = access_token
        else:
            raise ValueError("Username and password or access token must be supplied.")
            
    
    # Generic function to handle Particle Cloud API calls
    def api(self, method, url, data={}, params={}, headers={}):
        
        if method.upper() == 'GET':
            params_str = '&'.join(['%s=%s' % (k, v) for k, v in params.items()])
        
            response = requests.get(url + '?' + params_str)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data, headers=headers)
            
        response_obj = json.loads(response.text)

        if response.status_code != 200:
            if 'error_description' in response_obj:
                raise Exception(response_obj['error_description'])

            if 'error' in response_obj:
                raise Exception(response_obj['error'])
        
        return response_obj
        
    # List devices the currently authenticated user has access to.
    #
    # Returns a dict containing the response: https://docs.particle.io/reference/api/#list-devices
    def list_devices(self):

        try:        
            devices_obj = self.api('GET', DEVICES_URL, params={'access_token': self.access_token})
        except:
            raise

        return devices_obj

        
    # Get the current value of a variable exposed by the device.
    #
    # Returns a dict containing the response: https://docs.particle.io/reference/api/#get-a-variable-value
    def get_variable(self, device_id, variable_name):      
        url = ''.join([DEVICES_URL, '/', device_id, '/', variable_name])
                
        try:        
            variable_obj = self.api('GET', url, params={'access_token': self.access_token})
        except:
            raise

        return variable_obj
    
    # Call a function exposed by the device.
    #
    # Returns a dict containing the response: https://docs.particle.io/reference/api/#call-a-function
    def call_function(self, device_id, function_name, arg, raw=False):      
        url = ''.join([DEVICES_URL, '/', device_id, '/', function_name])
                
        try:
            if raw:
                return_value_obj = self.api('POST', url, data={'arg': arg,' format': 'raw', 'access_token': self.access_token})  
            else:
                return_value_obj = self.api('POST', url, data={'arg': arg,'access_token': self.access_token})  
        except:
            raise

        return return_value_obj