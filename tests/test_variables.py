import unittest

import os
import pyparticle as pp

class TestDevices(unittest.TestCase):

    # Test requesting a list of devices
    def test_list_devices(self):
        particle_user = os.environ['PARTICLE_IO_USER']
        particle_password = os.environ['PARTICLE_IO_PASSWORD']

        particle = pp.Particle(particle_user, particle_password)

        try:
            devices = particle.list_devices()

            if len(devices) == 0:
                self.fail("Failed: no devices found")
        except Exception, error:
            self.fail("Failed with %s" % error)
