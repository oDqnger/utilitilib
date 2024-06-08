import unittest
from ..are_anagrams import are_anagrams

class TestAreAnagrams(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
            [["silent", "listen"], True],
            [["Hello", "World"], False],
            [["cinema", "iceman"], True],
        ]

    def test_valid_cases(self):
        for x in self.valid_test_cases:
            self.assertEqual(are_anagrams(x[0][0], x[0][1]), x[1])
    
if __name__ == "__main__":
    unittest.main()
