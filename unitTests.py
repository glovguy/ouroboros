import unittest
from mock import MagicMock, patch
from nodeFactory import *
from circularity import *


class test_node_factory(unittest.TestCase):
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


class test_circularity(unittest.TestCase):
    def test_loop_find_visitor_keeps_track_of_visited_nodes(self):
        visitor = LoopFindVisitor()
        visitor.visit('nodename', [])
        self.assertTrue(visitor.node_visited('nodename'))

    def test_loop_find_visitor_identifies_loop(self):
        visitor = LoopFindVisitor()
        self.assertTrue(visitor.visit('n3', ['n1', 'n2', 'n3', 'n4']))
        self.assertEqual(visitor.loops, [['n3', 'n4', 'n3']])


if __name__ == '__main__':
    unittest.main(verbosity=1)
