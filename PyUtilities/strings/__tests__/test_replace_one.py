import unittest
from ..replace_one import replace_one

class TestReplaceOne(unittest.TestCase):
    def setUp(self):
        self.test_valid_cases = [
            ["hello world", "o", ".", "hello w.rld"],
            ["10,000.67", ".", ",", "10,000,67"]
        ]

    def test_valid_cases(self):
        for x in self.test_valid_cases:
            self.assertEqual(replace_one(x[0], x[1], x[2]), x[3])

if __name__ == "__main__":
    unittest.main()
