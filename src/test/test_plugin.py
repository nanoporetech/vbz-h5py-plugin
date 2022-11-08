"""
Test the vbz_h5py_plugin module
"""
# Disable pylint unavoidable pylint warnings
# pylint: disable=E0401,E1101,W0611,C0415

from pathlib import Path
import unittest
import h5py


TEST_FILE = Path(__file__).parent / "vbz_reads.fast5"


class TestPlugin(unittest.TestCase):
    """Test the plugin works"""

    def read_signal(self):
        """Reads some signal from a vbz compressed fast5 file"""
        self.assertTrue(TEST_FILE.exists())

        has_tested_read = False
        with h5py.File(TEST_FILE, "r") as h5_file:
            for group in h5_file:
                if group.startswith("read_"):
                    signal = h5_file[group + "/Raw/Signal"][0:]
                    self.assertTrue(len(signal) > 0, "No signal data to test!")

                    has_tested_read = True

        if not has_tested_read:
            self.fail("Didn't test any data!")

    # unittest with always run this test first as it's alphabetically sorted
    def test_h5py_fails_without_plugin(self):
        """Assert that a vbz compressed read fails to be loaded without the plugin"""
        assert TEST_FILE.exists()

        with self.assertRaisesRegex(OSError, "Can't read data"):
            self.read_signal()

    def test_h5py_passes_with_plugin(self):
        """Assert that a vbz compressed read can be loaded"""
        assert TEST_FILE.exists()

        # Pretty hacky implementation but this test is always run second.
        import vbz_h5py_plugin

        self.read_signal()
