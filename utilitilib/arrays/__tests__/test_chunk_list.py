import unittest
from ..chunk_list import chunk_list

class TestChunkList(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9]]],
            [[1, 2, 3, 4, 5, 6, 7], 2, [[1, 2], [3, 4], [5, 6], [7]]],
            [[],1, []],
            [[1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]]
        ]
    
    def test_valid_cases(self):
        for x in self.valid_test_cases:
            self.assertEqual(chunk_list(x[0], x[1]), x[2])

if __name__ == "__main__":
    unittest.main()
