# pyparticle
pyParticle is a Python library that allows you to interacts with particle.io devices. Currently the library and connect to the particle cloud API, list devices, read variables that a device has published, and called functions that a device has exposed.

Please find an example project here: [http://www.howardpaget.co.uk/blog/2016/08/26/pyparticle-a-python-library-for-interacting-with-particle-iot-devices/](http://www.howardpaget.co.uk/blog/2016/08/26/pyparticle-a-python-library-for-interacting-with-particle-iot-devices/)

##Installation

```pip install git+https://github.com/hejp89/pyparticle.git```

## Examples

### Connecting to the Cloud API

The Particle object is main object to access the particle.io cloud API it can be created by passing a login details or an access token.

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

A variable is created on the device like so:

```C
Particle.variable("humidity", humidity);

//..

float h = dht.getHumidity();
if(!isnan(h) && h > 0)
    humidity = h;
```

### Call a function
```Python
water_plant_result = particle.call_function(device['id'], 'water_plant', 10)
print('Water plant result: %s' % water_planet_result['return_value'])
```

A function is exposed on the device like so:

```C
Particle.function("set_led", setLED);

// ..

int setLED(String command){
    if(command == "on"){
        digitalWrite(D6, HIGH);
        return 1;
    }else if(command == "off"){
        digitalWrite(D6, LOW);
        return 0;
    }
    return -1;
}
```

