import unittest
import shutil
import os
from os import path

from dirpart import part

class TestDirPart(unittest.TestCase):
    TEST_FOLDER = "test-data"

    @property
    def _test_path(self):
        return path.join(os.getcwd(), self.TEST_FOLDER)

    def _put_file(self, f):
        # Create an empty file with the given name
        full = path.join(self._test_path, f)
        os.mknod(full)

    def setUp(self):
        # Delete the test-data folder
        td_dir = self._test_path

        if path.exists(td_dir):
            shutil.rmtree(td_dir)

        os.makedirs(td_dir)

    def test_discover_files(self):
        self._put_file("file1")
        self._put_file("file2")
        result = list(part.discover_files(self._test_path))

        self.assertEqual(len(result), 2)
        self.assertEqual("file1", result[0])
        self.assertEqual("file2", result[1])

    def test_part_files_creates_directories(self):
        self._put_file("a file")
        self._put_file("banana")
        p = self._test_path
        part.part_files(p)

        self.assertTrue(path.isdir(
            path.join(p, "A")))

        self.assertTrue(path.isdir(
            path.join(p, "B")))

    def test_part_files_copies_files(self):
        self._put_file("a file")
        self._put_file("banana")
        p = self._test_path
        part.part_files(p)

        # Make sure the files got copies
        self.assertTrue(path.isfile(
            path.join(p, "A", "a file")))

        self.assertTrue(path.isfile(
            path.join(p, "B", "banana")))

        # ... And not moved
        self.assertTrue(path.isfile(
            path.join(p, "a file")))

        self.assertTrue(path.isfile(
            path.join(p, "banana")))

if __name__ == '__main__':
    unittest.main()
