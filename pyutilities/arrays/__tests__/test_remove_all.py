import unittest
from ..remove_all import remove_all

class TestRemoveAll(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
            [[[3,7,2,2,1,1,11,1], 1], [3,7,2,2,11]],
            [[[5,5,5,5,5,5,5,5], 5], []],
            [[[1235,345345,1235457,6234], 6234], [1235,345345,1235457]],
            [[["something", "this", "is", "something", "cool"], "something"], ["this", "is", "cool"]],
            [[["a", "b", "c", "d"], "a"], ["b", "c", "d"]],
            [[[True, True, False], True], [False]],
            [[[], 5], []],
        ]

    def test_valid_cases(self):
        for x in self.valid_test_cases:
            self.assertEqual(remove_all(x[0][0], x[0][1]), x[1])

if __name__ == "__main__":
    unittest.main()
