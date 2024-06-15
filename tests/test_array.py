import unittest

from utilitilib.arrays import (
    chunk_list,
    remove_all,
    remove_duplicate,
    shuffle,
    unique_value_counter
)

class TestArrays(unittest.TestCase):
    def setUp(self):
        self.chunk_list_tests = [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [[1, 2, 3, 4], [5, 6, 7, 8], [9]]],
            [[1, 2, 3, 4, 5, 6, 7], 2, [[1, 2], [3, 4], [5, 6], [7]]],
            [[],1, []],
            [[1, 2, 3, 4, 5], 1, [[1], [2], [3], [4], [5]]]
        ]

        self.remove_all_test_cases = [
            [[[3,7,2,2,1,1,11,1], 1], [3,7,2,2,11]],
            [[[5,5,5,5,5,5,5,5], 5], []],
            [[[1235,345345,1235457,6234], 6234], [1235,345345,1235457]],
            [[["something", "this", "is", "something", "cool"], "something"], ["this", "is", "cool"]],
            [[["a", "b", "c", "d"], "a"], ["b", "c", "d"]],
            [[[True, True, False], True], [False]],
            [[[], 5], []],
        ]

        self.remove_expected_test_cases = [
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
        
        self.remove_not_expected_test_cases = [
            [[1,1,1,2,2,2,3,3,3], [1,1,1,2,2,2,3,3,3]],
        ]

        self.shuffle_expected_test_cases = [
            [[1,2,3,4,5], [1,2,3,4,5]],
            [[3,5,6,2,1], [6,2,1,6,2]],
            [[0,231,323123,534534,312312], [0,231,323123,534534,312312]],
            [[True, False, 1,2, "hello", "world"], [2,1,True, False,"world", "hello"]],
        ]
        
        self.shuffle_not_expected_test_cases = [
            [[], []]
        ]

        self.unique_value_valid_test_cases = [
            [[1,2,3,1,2,3,4,5,1,2,2], {2:4,1:3,3:2,4:1,5:1}],
            [[0,0,0,0,0,0], {0:6}],
            [[], {}],
            [['a','b','a','c','b','a','d'], {'a':3,'b':2,'c':1,'d':1}],
            [[1,2,3,3,3,3,'a','a'], {1:1,2:1,3:4,"a":2}],
            [["True", "False", "True", "None", "None", "None", 5, 5, 69], {"True": 2, "False": 1, "None": 3, 5: 2, 69: 1}]
        ]

    def test_chunk_list(self):
        for x in self.chunk_list_tests:
            self.assertEqual(chunk_list.chunk_list(x[0], x[1]), x[2])

    def test_remove_all(self):
        for x in self.remove_all_test_cases:
            self.assertEqual(remove_all.remove_all(x[0][0], x[0][1]), x[1])

    def test_remove_duplicate(self):
        for test in self.remove_expected_test_cases:
            self.assertEqual(remove_duplicate.remove_duplicate(test[0]), test[1])

        for test in self.remove_not_expected_test_cases:
            self.assertNotEqual(remove_duplicate.remove_duplicate(test[0]), test[1])

    def test_shuffle(self):
        for test in self.shuffle_expected_test_cases:
            self.assertNotEqual(shuffle.shuffle(test[0]), test[1])
            self.assertEqual(len(shuffle.shuffle(test[0])), len(test[1]))
            self.assertTrue(shuffle.shuffle(test[0])[2] in test[0])

        for test in self.shuffle_not_expected_test_cases:
            self.assertEqual(shuffle.shuffle(test[0]), test[1])
            self.assertEqual(len(shuffle.shuffle(test[0])), len(test[1]))

    def test_unique_value(self):
        for x in self.unique_value_valid_test_cases:
            self.assertEqual(unique_value_counter.unique_value_counter(x[0]), x[1])

if __name__ == "__main__":
    unittest.main()
