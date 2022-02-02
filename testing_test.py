from testing import fixname
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(fixname(testcase), expected)
    
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(fixname(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(fixname(testcase), expected)

    def test_onr_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(fixname(testcase), expected)

unittest.main()