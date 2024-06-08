import unittest
from ..range import range

class TestRangeMethod(unittest.TestCase):
    
    def setUp(self):
        self.valid_range_test_cases = [
            [[1,2,3,4,5,6],5],
            [[431,235,21,52,342,532,21],511],
            [[8,11,5,9,7,6,3616], 3611],
            [[3,4,5,6,7,8,9], 6],
            [[13, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16], 3],
        ]
        
        self.invalid_range_test_cases = [
            [[1,2,3,4, "float"], 3]
        ]
    
    def test_valid_range(self):
        for x in self.valid_range_test_cases:
            self.assertEqual(range(x[0]), x[1])
            
    def test_invalid_range(self):
        for x in self.invalid_range_test_cases:
            with self.assertRaises(TypeError):
                range(x[0])
            
if __name__ == "__main__":
    unittest.main()
