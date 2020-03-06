import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def test_solution(self):
        inst = Solution()
        self.assertTrue(inst.isValid("()"))
        self.assertTrue(inst.isValid("()[]{}"))
        self.assertTrue(inst.isValid("{[]}"))

        self.assertFalse(inst.isValid("(]"))
        self.assertFalse(inst.isValid("([)]"))
