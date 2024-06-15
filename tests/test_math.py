import unittest

from utilitilib.math import (
    mean,
    mode,
    range,
    median
)

class TestMath(unittest.TestCase):
    def setUp(self): 
        self.test_mean_cases = [
            [[1,1,1,1,1,1], 1],
            [[15, 13, 18, 16, 14, 17, 12], 15],
            [[6, 2, 3], 11/3],
            [[6.5, 2.3, 75.3, 24.6, 2.22, 634.2231, 582.02, 69.0], 174.5203875],
            [[-5, -2, 2, 4, -2], -0.6],
            [[True, False, True, False, False, True, False, False], 0.375],
        ]
        
        self.test_invalid_mean_cases = [
            [],
            ["dasdas", 42, 321,21],
            1,
            [[],[],[],[]],
        ]

        self.median_valid_cases = [
            [[1, 3, 5, 7, 9], 5],
            [[2,4,6,6], 5.0],
            [[6,3,7,5,1,3,5], 5],
            [[-5, -3, 0, 2, 4], 0],
            [[1, 1, 2, 2, 3, 3], 2],
            [[5], 5],
            [[], None]
        ]

        self.mode_valid_cases = [
            [[2,2,3,1], 2],
            [[1,1,2,3,3,3], 3],
            [[5,2,6,6,2,1,1,3,8,8,8,8], 8],
            [[6,231,6324,1272,53,31,643], None],
            [[2,1,3,4,5,6,7], None],
            [[5234234,28736482734,5312, 5312, 5234234], [5234234, 5312]],
            [[5,5,3,3,2,1,65,8,6], [5,3]],
            [["idot", "hello", "bozo", "bozo", "blue", "ping", "ping", "bozo", "bozo"], "bozo"],
            [[True, True, False, True], True],
            [["idot", "idot", 2, 3,3], [3,"idot"]],
        ]
        
        self.mode_invalid_cases = [
            [283428934283649862836482638462873648268346826348623984628364892634, 2],
            123,
        ]

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

    def test_valid_mean(self):
        for test in self.test_mean_cases:
            self.assertEqual(mean.mean(test[0]), test[1])
    
    def test_invalid_mean(self):
        for test in self.test_invalid_mean_cases:
            with self.assertRaises(Exception):
                mean.mean(test)

    def test_valid_median(self):
        for test_case in self.median_valid_cases:
            self.assertEqual(median.median(test_case[0]), test_case[1])

    def test_valid_mode(self):
        for test in self.mode_valid_cases:
            self.assertEqual(mode.mode(test[0]), test[1])
    
    def test_invalid_mode(self):
        for test in self.mode_invalid_cases:
            with self.assertRaises(Exception):
                mode.mode(test)

    def test_valid_range(self):
        for x in self.valid_range_test_cases:
            self.assertEqual(range.range(x[0]), x[1])
            
    def test_invalid_range(self):
        for x in self.invalid_range_test_cases:
            with self.assertRaises(TypeError):
                range.range(x[0])

if __name__ == "__main__":
    unittest.main()

