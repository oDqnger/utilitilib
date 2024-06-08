import unittest
from ..mode import mode

class TestModeMethod(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
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
        
        self.invalid_test_cases = [
            [283428934283649862836482638462873648268346826348623984628364892634, 2],
            123,
        ]
    
    def test_valid_mode(self):
        for test in self.valid_test_cases:
            self.assertEqual(mode(test[0]), test[1])
    
    def test_invalid_mode(self):
        for test in self.invalid_test_cases:
            with self.assertRaises(Exception):
                mode(test)
                
if __name__ == "__main__":
    unittest.main()
