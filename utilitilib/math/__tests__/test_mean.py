import unittest
from ..mean import mean

class TestMeanMethod(unittest.TestCase):
    
    def setUp(self):
        self.valid_test_cases = [
            [[1,1,1,1,1,1], 1],
            [[15, 13, 18, 16, 14, 17, 12], 15],
            [[6, 2, 3], 11/3],
            [[6.5, 2.3, 75.3, 24.6, 2.22, 634.2231, 582.02, 69.0], 174.5203875],
            [[-5, -2, 2, 4, -2], -0.6],
            [[True, False, True, False, False, True, False, False], 0.375],
        ]
        
        self.invalid_test_cases = [
            [],
            ["dasdas", 42, 321,21],
            1,
            [[],[],[],[]],
        ]
        
    def test_valid_mean(self):
        for test in self.valid_test_cases:
            self.assertEqual(mean(test[0]), test[1])
    
    def test_invalid_mean(self):
        for test in self.invalid_test_cases:
            with self.assertRaises(Exception):
                mean(test)
        
if __name__ == "__main__":
    unittest.main()
