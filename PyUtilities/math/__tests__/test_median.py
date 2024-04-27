import unittest
from ..median import median

class TestMedianMethod(unittest.TestCase):
    def setUp(self):
        self.valid_cases = [
            [[1, 3, 5, 7, 9], 5],
            [[2,4,6,6], 5.0],
            [[6,3,7,5,1,3,5], 5],
            [[-5, -3, 0, 2, 4], 0],
            [[1, 1, 2, 2, 3, 3], 2],
            [[5], 5],
            [[], None]
        ]
    
    def test_valid_cases(self):
        for test_case in self.valid_cases:
            self.assertEqual(median(test_case[0]), test_case[1])

if __name__ == "__main__":
    unittest.main()
