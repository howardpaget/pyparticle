import unittest

from test_login import TestLogin

def suite():
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_login"))
    return unittest.makeSuite(TestLogin, 'test')
    # return suite

if __name__ == '__main__':
    unittest.main()
