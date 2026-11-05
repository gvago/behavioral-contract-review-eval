import time
import unittest
from threading import Event, Timer
from workspace.worker import start_export


class ExportTests(unittest.TestCase):
    def test_export(self):
        output, release = [], Event()
        thread = start_export(output, release)
        timer = Timer(0.1, release.set)
        timer.start()
        try:
            time.sleep(0.01)
            self.assertEqual(output, ['ready'])
            self.assertFalse(thread.is_alive(), 'export did not finish within test deadline')
        finally:
            release.set()
            thread.join(timeout=2)
            timer.join(timeout=2)
