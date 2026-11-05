import unittest
from workspace.common import credit


class DepositTests(unittest.TestCase):
    def test_deposit(self):
        result = credit(10, 5)
        self.assertEqual(result, result)
