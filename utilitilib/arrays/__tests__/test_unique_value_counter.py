import unittest
from ..unique_value_counter import unique_value_counter

class TestUniqueValueCounter(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
            [[1,2,3,1,2,3,4,5,1,2,2], {2:4,1:3,3:2,4:1,5:1}],
            [[0,0,0,0,0,0], {0:6}],
            [[], {}],
            [['a','b','a','c','b','a','d'], {'a':3,'b':2,'c':1,'d':1}],
            [[1,2,3,3,3,3,'a','a'], {1:1,2:1,3:4,"a":2}],
            [["True", "False", "True", "None", "None", "None", 5, 5, 69], {"True": 2, "False": 1, "None": 3, 5: 2, 69: 1}]
        ]

    def test_valid_cases(self):
        for x in self.valid_test_cases:
            self.assertEqual(unique_value_counter(x[0]), x[1])

if __name__ == "__main__":
    unittest.main()
