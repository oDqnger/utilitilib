from ..remove_duplicate import remove_duplicate
import unittest

class TestRemoveDuplicateMethod(unittest.TestCase):
    
    def setUp(self):
        self.expected_test_cases = [
            [[1,2,1,1,1,2,2,2,3,3,3], [1,2,3]],
            [[4,4,4,8,8,32,32,64,1,65, 100], [4,8,32,64,1,65,100]],
            [[1,2,3,4,5], [1,2,3,4,5]],
            [[1,1,1,1,1,1,1,1,1,1,1], [1]],
            [["true", "true", "balls", "nuts", "nuts", "nuts"], ["true", "balls", "nuts"]],
            [[True, True, True, False, False], [True, False]],
            [[1,1,1,2,2,2,3], [1,2,3]],
            [["Hello", "Hello", True, False, False, False, False, 2,2,2, 3], ["Hello", True, False, 2, 3]],
            [[], []]
        ]
        
        self.not_expected_test_cases = [
            [[1,1,1,2,2,2,3,3,3], [1,1,1,2,2,2,3,3,3]],
        ]
        
    def test_remove_duplicate_method_true(self):
        for test in self.expected_test_cases:
            self.assertEqual(remove_duplicate(test[0]), test[1])

    def test_remove_duplicate_method_false(self):
        for test in self.not_expected_test_cases:
            self.assertNotEqual(remove_duplicate(test[0]), test[1])

if __name__ == "__main__":
    unittest.main()
