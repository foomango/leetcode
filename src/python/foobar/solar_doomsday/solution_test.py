#!/usr/bin/env python
import unittest
from solution import answer
class TestSolution(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer(12), [9, 1, 1, 1])
        self.assertEqual(answer(15324), [15129, 169, 25, 1])

if __name__ == '__main__':
    unittest.main()
