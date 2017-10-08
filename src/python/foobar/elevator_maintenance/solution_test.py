#!/usr/bin/env python
import unittest
from solution import answer
class TestSolution(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]),
                ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"])
        self.assertEqual(answer(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1",
            "1.1.1", "2.0"]), ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2",
                "2.0", "2.0.0"])

if __name__ == '__main__':
    unittest.main()
