import unittest
from ..to_title_case import to_title_case

class TestToTitleCase(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases = [
            ["why i pooped my pants", "Why I Pooped My Pants"],
            ["I AM SO DUMB", "I Am So Dumb"],
            ["Hello My Name Is", "Hello My Name Is"],
            ["", ""]
        ]

    def test_valid_cases(self):
        for x in self.valid_test_cases:
            self.assertEqual(to_title_case(x[0]), x[1])
    
if __name__ == "__main__":
    unittest.main()
