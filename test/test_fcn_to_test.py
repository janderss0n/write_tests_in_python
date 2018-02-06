import unittest

import fcns_to_test

class TestFcns(unittest.TestCase):
    def setUp(self):
        self.nbr_1 = float(4)
        self.nbr_2 = float(5)
        self.nbr_3 = float(6.4)

    def test_add_numbers(self):
        self.assertEqual(fcns_to_test.add_numbers(self.nbr_1, self.nbr_2), float(9),
            'Incorrect addition')
        self.assertEqual(fcns_to_test.add_numbers(self.nbr_2, self.nbr_3), float(11.4),
            'Incorrect addition')
