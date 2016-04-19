# -*- coding: utf-8 -*-

import pyparticle as pp
import sys
import os

currenr_dir = os.path.dirname(__file__)
token_filename = os.path.join(currenr_dir, 'access_token.txt')

access_token_file = open(token_filename, 'r')
access_token = access_token_file.read().strip()
access_token_file.close()

particle = pp.Particle(access_token=access_token)

try:
    devices = particle.list_devices()
except:
    particle = pp.Particle('username', 'password')

    access_token_file = open(token_filename, 'w')
    access_token = access_token_file.write(particle.access_token)
    access_token_file.close()
    
    devices = particle.list_devices()

if len(devices) == 0:
    print('No devices found')
    sys.exit()
  
device = devices[0]

print('Selected device: %s' % device['name'])

humidity = particle.get_variable(device['id'], 'humidity')
temp_dht = particle.get_variable(device['id'], 'temp_dht')
temp_bmp = particle.get_variable(device['id'], 'temp_bmp')
pressure = particle.get_variable(device['id'], 'pressure')

print('Humidity: %.2f%%' % humidity['result'])
print('Temperature (DHT Sensor): %.2f°C' % temp_dht['result'])
print('Temperature (BMP Sensor): %.2f°C' % temp_bmp['result'])
print('Pressure: %.2fmb' % pressure['result'])
