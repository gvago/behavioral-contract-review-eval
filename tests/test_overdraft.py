import unittest
from workspace.common import credit


class OverdraftTests(unittest.TestCase):
    @unittest.skip('temporary')
    def test_overdraft(self):
        self.assertEqual(credit(10, -15), -5)
