import unittest
from unittest.mock import Mock
from workspace.common import notify


class NotificationTests(unittest.TestCase):
    def test_notify(self):
        sender = Mock()
        notify(sender)
        sender.send.assert_called_once_with('done')
