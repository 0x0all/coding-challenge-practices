#!/usr/bin/env python
import unittest
import os.path

from rolodex import file_to_str, process_entries

class TestRolodexMethods(unittest.TestCase):

    def test_readfile(self):
        self.assertTrue(isinstance(file_to_str('test.in'), list))

    def test_process_file(self):
        entries = process_entries(file_to_str('test.in'))
        self.assertEqual(len(entries['entries']), 3)
        self.assertEqual(len(entries['errors']), 5)

if __name__ == '__main__':
    unittest.main()