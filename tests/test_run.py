import unittest

from test_login import TestLogin
from test_devices import TestDevices
from test_function import TestFunction

def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestLogin, 'test'))
    suite.addTest(unittest.makeSuite(TestDevices, 'test'))
    suite.addTest(unittest.makeSuite(TestDFunction, 'test'))

    return suite

if __name__ == '__main__':
    unittest.main()
