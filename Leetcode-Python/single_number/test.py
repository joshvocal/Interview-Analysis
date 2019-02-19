import unittest
from solution import Solution
from solution import Solution2


class TestSolution(unittest.TestCase):

    def test_example_1(self):
        nums = [2, 2, 1]

        actual = Solution().singleNumber(nums)
        actual2 = Solution2().singleNumber(nums)
        expected = 1

        self.assertEquals(actual, expected)
        self.assertEquals(actual2, expected)

    def test_example_2(self):
        nums = [4, 1, 2, 1, 2]

        actual = Solution().singleNumber(nums)
        actual2 = Solution2().singleNumber(nums)
        expected = 4

        self.assertEquals(actual, expected)
        self.assertEquals(actual2, expected)

    def test_one_nums(self):
        nums = [1]

        actual = Solution().singleNumber(nums)
        actual2 = Solution().singleNumber(nums)
        expected = 1

        self.assertEquals(actual, expected)
        self.assertEquals(actual2, expected)
