import unittest
from threading import Event
from workspace.worker import start_export


class ExportTests(unittest.TestCase):
    def test_export(self):
        output, release = [], Event()
        thread = start_export(output, release)
        release.set()
        try:
            thread.join(timeout=2)
            self.assertFalse(thread.is_alive(), 'export did not finish within test deadline')
            self.assertEqual(output, ['ready'])
        finally:
            release.set()
            thread.join(timeout=2)
