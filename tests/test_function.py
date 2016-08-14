import unittest

import os
import pyparticle as pp

class TestFunction(unittest.TestCase):

    # Test calling a function of a device
    def test_function(self):
        particle_user = os.environ['PARTICLE_IO_USER']
        particle_password = os.environ['PARTICLE_IO_PASSWORD']

        particle = pp.Particle(particle_user, particle_password)

        device = particle.list_devices()[0]

        try:
            result1 = particle.call_function(device['id'], 'set_led', 'on')
            result2 = particle.call_function(device['id'], 'set_led', 'off')

            self.assertEqual(result1, 1)
            self.assertEqual(result2, 0)
        except Exception, error:
            self.fail("Failed with %s" % error)
