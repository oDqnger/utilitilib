import unittest
from datetime import date

from utilitilib.dateandtime import (
    days_between_dates,
)

class TestDateAndTime(unittest.TestCase):
    def setUp(self):
        self.days_between_dates_cases = [
            [[date(2020, 5, 6), date(2024, 6, 5)], 1491],         
            [[date(2024, 1, 1), date(2024, 1, 2)], 1]
        ]

    def test_days_between_dates(self):
        for x in self.days_between_dates_cases:
            self.assertEqual(days_between_dates.days_between_dates(x[0][0], x[0][1]), x[1])

if __name__ == "__main__":
    unittest.main()
