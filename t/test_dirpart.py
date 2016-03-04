# Author: Eric Lavesson

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

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "")

        self.assertTrue(path.isdir(
            path.join(p, "A")))
        self.assertTrue(path.isdir(
            path.join(p, "B")))

    def test_part_files_copies_files(self):
        self._put_file("a file")
        self._put_file("banana")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "")

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

    def test_part_files_creates_output_dir(self):
        self._put_file("abc")
        self._put_file("bcd")
        ip = self._test_path
        op = path.join(ip, "out")

        part.part_files(
            indir   = ip,
            outdir  = op,
            pattern = "")

        self.assertTrue(path.exists(op))

    def test_part_files_copies_files_to_output_dir(self):
        self._put_file("abc")
        self._put_file("bcd")
        ip = self._test_path
        op = path.join(ip, "out")

        part.part_files(
            indir   = ip,
            outdir  = op,
            pattern = "")

        self.assertTrue(path.isfile(
            path.join(op, "A", "abc")))
        self.assertTrue(path.isfile(
            path.join(op, "B", "bcd")))

    def test_part_files_moves_when_specified(self):
        self._put_file("a file")
        self._put_file("banana")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "",
            move    = True)

        # Make sure the files got moved
        self.assertTrue(path.isfile(
            path.join(p, "A", "a file")))
        self.assertTrue(path.isfile(
            path.join(p, "B", "banana")))

        # ... And not copied
        self.assertFalse(path.isfile(
            path.join(p, "a file")))
        self.assertFalse(path.isfile(
            path.join(p, "banana")))

    def test_part_files_multiple_files_copied(self):
        self._put_file("abc")
        self._put_file("abd")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "")

        self.assertTrue(path.isfile(
            path.join(p, "A", "abc")))
        self.assertTrue(path.isfile(
            path.join(p, "A", "abd")))

    def test_part_files_uses_regexp(self):
        self._put_file("123")
        self._put_file("abc")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "[A-z]")

        self.assertTrue(path.isfile(
            path.join(p, "A", "abc")))
        self.assertFalse(path.exists(
            path.join(p, "1", "123")))

    def test_part_files_handles_special_folders(self):
        self._put_file(".a_file")
        self._put_file("..a_file")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "")

        self.assertTrue(path.isfile(
            path.join(p, "!misc", ".a_file")))
        self.assertTrue(path.isfile(
            path.join(p, "!misc", "..a_file")))

    def test_part_files_can_change_special_folder(self):
        self._put_file(".a_file")
        p = self._test_path

        part.part_files(
            indir   = p,
            outdir  = p,
            pattern = "",
            special = 'special')

        self.assertTrue(path.isfile(
            path.join(p, "special", ".a_file")))

if __name__ == '__main__':
    unittest.main()
