import unittest
from ..censor_string import censor_string

class TestCensorStringMethod(unittest.TestCase):
    def setUp(self):
        self.default_valid_test_cases = [
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
        
    def test_valid_cases(self):
        for x in self.default_valid_test_cases:
            self.assertEqual(censor_string(x[0]), x[1])

    def test_custom_test_cases(self):
        for x in self.custom_char_test_cases:
            self.assertEqual(censor_string(x[0], censor_char=x[1]), x[2])

        for x in self.custom_char_amount_test_cases:
            self.assertEqual(censor_string(x[0], censor_char_amount=x[1]), x[2])
        
        for x in self.custom_swear_word_test_cases:
            self.assertEqual(censor_string(x[0], custom_swear_words=x[1]), x[2])
        
        for x in self.custom_addition_swear_word_cases:
            self.assertEqual(censor_string(x[0], addition_swear_words=x[1]), x[2])
        
if __name__ == "__main__":
    unittest.main()
    