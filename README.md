# pyparticle
Python SDK for Particle.io. Currently the SDK implements listing devices, getting a variable value, and calling a function these will likely be enough for most projects.

## Examples

### Connecting to the Cloud API
```Python
import pyparticle as pp

particle = pp.Particle(access_token=access_token)

# or

particle = pp.Particle('username', 'password')
```

### List devices
```Python
devices = particle.list_devices()

print('Found %d device(s)' % len(devices))
```

### Get a variable value
```Python
device = devices[0]
print('Selected device: %s' % device['name'])

humidity = particle.get_variable(device['id'], 'humidity')
print('Humidity: %.2f%%' % humidity['result'])
```

### Call a function
```Python
water_plant_result = particle.call_function(device['id'], 'water_plant', 10)
print('Water plant result: %s' % water_planet_result['return_value'])
```

