from ..shuffle import shuffle
import unittest

class TestShuffleMethod(unittest.TestCase):

    def setUp(self):
        self.expected_test_cases = [
            [[1,2,3,4,5], [1,2,3,4,5]],
            [[3,5,6,2,1], [6,2,1,6,2]],
            [[0,231,323123,534534,312312], [0,231,323123,534534,312312]],
            [[True, False, 1,2, "hello", "world"], [2,1,True, False,"world", "hello"]],
        ]
        
        self.not_expected_test_cases = [
            [[], []]
        ]
    
    def test_shuffle_expected(self):
        for test in self.expected_test_cases:
            self.assertNotEqual(shuffle(test[0]), test[1])
            self.assertEqual(len(shuffle(test[0])), len(test[1]))
            self.assertTrue(shuffle(test[0])[2] in test[0])
    
    def test_shuffle_not_expected(self):
        for test in self.not_expected_test_cases:
            self.assertEqual(shuffle(test[0]), test[1])
            self.assertEqual(len(shuffle(test[0])), len(test[1]))
    
if __name__ == "__main__":
    unittest.main()
