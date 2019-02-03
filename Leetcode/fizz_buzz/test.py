import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_example(self):
        n = 15

        actual = Solution().fizzBuzz(n)
        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ]

        self.assertEqual(actual, expected)
