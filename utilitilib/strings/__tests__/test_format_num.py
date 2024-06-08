import unittest
from ..format_num import format_num

class TestFormatNum(unittest.TestCase):
    def setUp(self):
        self.valid_test_cases_with_default = [
            [1000, "1,000"],
            [10000, "10,000"],
            [100000, "100,000"],
            [1000000, "1,000,000"],
            [10000000, "10,000,000"],
            [100000000, "100,000,000"],
            [1000000000, "1,000,000,000"],
            [10000000000, "10,000,000,000"],
            [100000000000, "100,000,000,000"],
            [-1000, "-1,000"],
            [-10000, "-10,000"],
            [-100000, "-100,000"],
            [-1000000, "-1,000,000"],
            [-10000000, "-10,000,000"],
            [-100000000, "-100,000,000"],
            [-1000000000, "-1,000,000,000"],
            [-10000000000, "-10,000,000,000"],
            [-100000000000, "-100,000,000,000"],
            [234, "234"],
            [10, "10"],
            [1, "1"],
            [-32542.32, "-32,542.32"]
        ]
        
        self.valid_test_cases_custom = [
            [1000, "1.000", ".", ".", "-"],
            [10000.67, "10,000,67", ",", ",", "-"],
            [-100000, "+100BALLS000", "BALLS", ".", "+"],
            [1000000, "13.140003.14000", "3.14", ".", "-"],
            [10000000, "10,000,000", ",", ".", "-"],
            [-53120.32, "NEGATIVE 53:120;32", ":", ";", "NEGATIVE "]
        ]

    def test_valid_cases(self):
        for x in self.valid_test_cases_with_default:
            self.assertEqual(format_num(x[0]), x[1])
           
        for x in self.valid_test_cases_custom:
            self.assertEqual(format_num(x[0], custom_comma=x[2], custom_decimal=x[3], custom_negative=x[4]), x[1])

        self.assertEqual(format_num(23000.32, custom_comma=".", custom_decimal="x"), "23.000x32")

if __name__ == "__main__":
    unittest.main()
