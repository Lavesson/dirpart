import unittest
import shutil
import os
from os import path

class TestDirPart(unittest.TestCase):
    def setUp(self):
        # Delete the test-data folder
        td_dir = path.join(os.getcwd(), "test-data")
        
        if path.exists(td_dir):
            shutil.rmtree(td_dir)

        os.makedirs(td_dir)

    def test_move(self):
        pass;

if __name__ == '__main__':
    unittest.main()
