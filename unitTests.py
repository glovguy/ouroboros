import unittest
from nodeFactory import pythonify_path

class test_statements(unittest.TestCase):
    def test_pythonify_path(self):
        self.assertEqual(pythonify_path('file.py'), 'file')
        self.assertEqual(pythonify_path('folder/file.py'), 'folder.file')
        self.assertEqual(
            pythonify_path('folder1/folder2/_file_with_symbols_.py'),
            'folder1.folder2._file_with_symbols_'
            )


if __name__ == '__main__':
    unittest.main(verbosity=1)
