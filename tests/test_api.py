import unittest
from api import sm


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method executes before each test run
        """
        self.app = sm.test_client(self)
