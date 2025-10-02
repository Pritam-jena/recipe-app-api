""" Simple test """

from django.test import SimpleTestCase
from app import cal

class calstest(SimpleTestCase):
    """ test the first simple code"""

    def test_add_number(self):
        """Add two number and return"""
        res = cal.add(5,6)

        self.assertEqual(res,11)