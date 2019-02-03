import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        s = "anagram"
        t = "nagaram"

        actual = Solution().isAnagram(s, t)
        expected = True

        self.assertEquals(actual, expected)

    def test_diff_length(self):
        s = "a"
        t = "ab"

        actual = Solution().isAnagram(s, t)
        expected = False

        self.assertEquals(actual, expected)
