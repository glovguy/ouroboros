import unittest
from nodeFactory import *


class test_statements(unittest.TestCase):
    def test_pythonify_path(self):
        self.assertEqual(pythonify_path('file.py'), 'file')
        self.assertEqual(pythonify_path('folder/file.py'), 'folder.file')
        self.assertEqual(
            pythonify_path('folder1/folder2/_file_with_symbols_.py'),
            'folder1.folder2._file_with_symbols_'
            )


    def test_ignore_node(self):
        self.assertEqual(ignore_node('nodename', []), False)
        self.assertEqual(ignore_node('nodename', [r'nodename']), True)
        self.assertEqual(ignore_node('name_of_node', [r'nonmatch', r'.+_of_node']), True)


    def test_hash_from_csv(self):
        self.assertEqual(
            hash_from_csv([['file', '', 'other_file']], []),
            { 'file': set(['other_file']) }
            )


if __name__ == '__main__':
    unittest.main(verbosity=1)
