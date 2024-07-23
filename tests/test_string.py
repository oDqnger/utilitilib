import unittest

from utilitilib.strings import (
    are_anagrams,
    censor_string,
    format_num,
    replace_one,
    to_title_case,
    remove_whitespace,
)

class TestStrings(unittest.TestCase):
    def setUp(self): 
        self.anagram_test_cases = [
            [["silent", "listen"], True],
            [["Hello", "World"], False],
            [["cinema", "iceman"], True],
        ]

        self.censor_default_valid_test_cases = [
            ["oh fuck", "oh ****"],
            ["oh shit", "oh ****"],
            ["you stupid bitch", "you stupid *****"],
            ["I FUCKING HATE THIS STUPID ASS JOB OMG SHIT", "i ****ing hate this stupid *** job omg ****"],
            ["nice cock :wink:", "nice **** :wink:"],
            ["dicking", "****ing"]
        ]
        
        self.custom_char_test_cases = [
            ["oh fuck you", ".", "oh .... you"],
            ["whats ur sex", "$", "whats ur $$$"],
            ["you stupid fucking bitch, cunt", "", "you stupid ing , "]
        ]

        self.custom_char_amount_test_cases = [
            ["oh fuck you", 1, "oh * you"],
            ["whats ur sex", 10, "whats ur **********"],
            ["you stupid fucking bitch, cunt", 3, "you stupid ***ing ***, ***"]
        ]
        
        self.custom_swear_word_test_cases = [
            ["kill yourself idiot", ["kill", "idiot"], "**** yourself *****"],
            ["fuck you bitch", ["something", "random"], "fuck you bitch"],
            ["you stupid fucking bitch, cunt", [], "you stupid ****ing *****, ****"],
            ["idiot", ["idiot"], "*****"]
        ]
        
        self.custom_addition_swear_word_cases = [
            ["kill yourself you fucking idiot", ["kill", "idiot"], "**** yourself you ****ing *****"],
            ["fuck you, you stupid random bitch", ["something", "random"], "**** you, you stupid ****** *****"],
            ["you stupid fucking bitch, cunt", [], "you stupid ****ing *****, ****"],
        ]

        self.format_valid_test_cases_with_default = [
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
        
        self.format_valid_test_cases_custom = [
            [1000, "1.000", ".", ".", "-"],
            [10000.67, "10,000,67", ",", ",", "-"],
            [-100000, "+100BALLS000", "BALLS", ".", "+"],
            [1000000, "13.140003.14000", "3.14", ".", "-"],
            [10000000, "10,000,000", ",", ".", "-"],
            [-53120.32, "NEGATIVE 53:120;32", ":", ";", "NEGATIVE "]
        ]

        self.replace_one_valid_cases = [
            ["hello world", "o", ".", "hello w.rld"],
            ["10,000.67", ".", ",", "10,000,67"]
        ]

        self.to_title_case_test_cases = [
            ["why i pooped my pants", "Why I Pooped My Pants"],
            ["I AM SO DUMB", "I Am So Dumb"],
            ["Hello My Name Is", "Hello My Name Is"],
            ["", ""]
        ]

        self.remove_whitespace_test_cases = [
            ["Hello World", "HelloWorld"],
            ["I am an idiot   fr        ", "Iamanidiotfr"],
            ["   ", ""]
        ]

    def test_anagram_valid_cases(self):
        for x in self.anagram_test_cases:
            self.assertEqual(are_anagrams.are_anagrams(x[0][0], x[0][1]), x[1])

    def test_censor_valid_cases(self):
        for x in self.censor_default_valid_test_cases:
            self.assertEqual(censor_string.censor_string(x[0]), x[1])

    def test_censor_custom_test_cases(self):
        for x in self.custom_char_test_cases:
            self.assertEqual(censor_string.censor_string(x[0], censor_char=x[1]), x[2])

        for x in self.custom_char_amount_test_cases:
            self.assertEqual(censor_string.censor_string(x[0], censor_char_amount=x[1]), x[2])
        
        for x in self.custom_swear_word_test_cases:
            self.assertEqual(censor_string.censor_string(x[0], custom_swear_words=x[1]), x[2])
        
        for x in self.custom_addition_swear_word_cases:
            self.assertEqual(censor_string.censor_string(x[0], addition_swear_words=x[1]), x[2])

    
    def test_format_test_valid_cases(self):
        for x in self.format_valid_test_cases_with_default:
            self.assertEqual(format_num.format_num(x[0]), x[1])
           
        for x in self.format_valid_test_cases_custom:
            self.assertEqual(format_num.format_num(x[0], custom_comma=x[2], custom_decimal=x[3], custom_negative=x[4]), x[1])

        #self.assertEqual(format_num.format_num(23000.32, custom_comma=".", custom_decimal="x"), "23.000x32")

    def test_replace_one_valid_cases_method(self):
        for x in self.replace_one_valid_cases:
            self.assertEqual(replace_one.replace_one(x[0], x[1], x[2]), x[3])

    def test_to_title_case_valid_cases(self):
        for x in self.to_title_case_test_cases:
            self.assertEqual(to_title_case.to_title_case(x[0]), x[1])

    def test_remove_whitespace_valid_cases(self):
        for x in self.remove_whitespace_test_cases:
            self.assertEqual(remove_whitespace.remove_whitespace(x[0]), x[1])

if __name__ == "__main__":
    unittest.main()

