import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        nums = [2, 2, 1]

        actual = Solution().singleNumber(nums)
        expected = 1

        self.assertEquals(actual, expected)

    def test_example_2(self):
        nums = [4, 1, 2, 1, 2]

        actual = Solution().singleNumber(nums)
        expected = 4

        self.assertEquals(actual, expected)

    def test_empty_nums(self):
        nums = []

        actual = Solution().singleNumber(nums)
        expected = None

        self.assertEquals(actual, expected)

    def test_one_nums(self):
        nums = [1]

        actual = Solution().singleNumber(nums)
        expected = 1

        self.assertEquals(actual, expected)
