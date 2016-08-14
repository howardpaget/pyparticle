import unittest

import sys
sys.path.insert(0, '../')

import os
import pyparticle as pp

class TestLogin(unittest.TestCase):

    # Test logging in with a valid login details
    def test_login(self):
        particle_user = os.environ['PARTICLE_IO_USER']
        particle_password = os.environ['PARTICLE_IO_PASSWORD']

        try:
            particle = pp.Particle(particle_user, particle_password)
        except Exception, error:
            self.fail("Failed with %s" % error)

    # Test creating a Particle instance with an access token
    def test_login_token(self):
        particle_user = os.environ['PARTICLE_IO_USER']
        particle_password = os.environ['PARTICLE_IO_PASSWORD']

        particle = pp.Particle(particle_user, particle_password)

        try:
            particle = pp.Particle(access_token=particle.access_token)
        except Exception, error:
            self.fail("Failed with %s" % error)

    # Test that using invalid login details raise a LoginError
    def test_login_invalid_details(self):
        particle_user = 'user@gmail.com'
        particle_password = 'pa$$word'

        with self.assertRaises(pp.LoginError):
            particle = pp.Particle(particle_user, particle_password)
