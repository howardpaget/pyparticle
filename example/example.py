# -*- coding: utf-8 -*-

import pyparticle as pp
import sys
import os

# Read the access token stored in a file
current_dir = os.path.dirname(__file__)
token_filename = os.path.join(currenr_dir, 'access_token.txt')

access_token_file = open(token_filename, 'r')
access_token = access_token_file.read().strip()
access_token_file.close()

# Initiatise the Particle object using the cache access token
particle = pp.Particle(access_token=access_token)

try:
    devices = particle.list_devices()
except:
    # An exception has been raised indicating that the access token is out of date use the login details to refresh the token
    particle = pp.Particle('username', 'password')

    # Cache the token for reuse
    access_token_file = open(token_filename, 'w')
    access_token = access_token_file.write(particle.access_token)
    access_token_file.close()

    devices = particle.list_devices()

if len(devices) == 0:
    print('No devices found')
    sys.exit()

# Use the first device in the list this device is running the dht-example.ino example
device = devices[0]

print('Found %d devices' % len(devices))

print('Selected device: %s' % device['name'])

# The device exposes the variables 'humidity', 'temp_dht', 'temp_bmp' and 'pressure'
humidity = particle.get_variable(device['id'], 'humidity')
temp_dht = particle.get_variable(device['id'], 'temp_dht')
temp_bmp = particle.get_variable(device['id'], 'temp_bmp')
pressure = particle.get_variable(device['id'], 'pressure')

# Print the variables
print('Humidity: %.2f%%' % humidity['result'])
print('Temperature (DHT Sensor): %.2f°C' % temp_dht['result'])
print('Temperature (BMP Sensor): %.2f°C' % temp_bmp['result'])
print('Pressure: %.2fmb' % pressure['result'])

# The device exposes the function set_led which takes in a command of either 'on' or 'off' and sets the LED to on or off
led_value = particle.call_function(device['id'], 'set_led', 'on')

# The set_led function returns a 0 or 1 if the LED is turned off or on, or -1 on an error e.g. invalid command
print('LED Value: %d' % led_value)
