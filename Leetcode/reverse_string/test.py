import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_real_word(self):
        s = "Hello World"

        actual = Solution().reverseString(s)
        expected = "dlroW olleH"

        self.assertEqual(actual, expected)

    def test_empty_string(self):
        s = ""

        actual = Solution().reverseString(s)
        expected = ""

        self.assertEqual(actual, expected)

    def test_null_string(self):
        s = None

        actual = Solution().reverseString(s)
        expected = None

        self.assertEqual(actual, expected)

    def test_one_letter(self):
        s = "a"

        actual = Solution().reverseString(s)
        expected = "a"

        self.assertEqual(actual, expected)
