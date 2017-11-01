import unittest
from testHelper import *
from nodeFactory import *
from circularity import *
from traversal import *

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
        self.assertEqual(visitor.loops, [('n3', 'n4')])

    def test_loop_find_visitor_does_not_identify_non_loop(self):
        visitor = LoopFindVisitor()
        self.assertNotEqual(visitor.visit('n3', ['n1', 'n2']), True)

    def test_loop_for(self):
        path = ['n1', 'n2', 'n3', 'n4']
        self.assertEqual(
            loop_for(path, 'n3'),
            ('n3', 'n4')
            )

    def test_find_loops(self):
        loops = find_loops({'n1': set(['n2']), 'n2': set(['n3']), 'n3': set(['n1'])})
        self.assertEqual(len(loops), 1)
        self.assertEqual(loops, [('n1', 'n2', 'n3')])

    def test_group_loops_by_module(self):
        loops = [
            ('1', '2'),
            ('3', '4'),
            ('1', '5', '6'),
            ('4', '7')
            ]
        groups = group_loops_by_module(loops)
        expected = {
            '1': set([
                ('1', '2'),
                ('1', '5', '6')
                ]),
            '4': set([
                ('3', '4'),
                ('4', '7')
                ])
            }
        self.assertEqual(groups, expected)

    def test_edges_from_loops(self):
        loops = [
            ('3', '4'),
            ('1', '5', '6'),
            ('4', '7')
            ]
        expectedEdges = [
            ('3', '4'), ('4', '3'), ('1', '5'), ('5', '6'),
            ('6', '1'), ('4', '7'), ('7', '4')
            ]
        self.assertEqual(edges_from_loops(loops), expectedEdges)


class test_traversal(unittest.TestCase):
    def test_breadth_first_search_visits_all_nodes_in_depth_first_order(self):
        visitor = MockVisitor()
        maxN = 5
        nodeHash = {str(x): str(x+1) for x in range(0, maxN)}
        nodeHash['1'] = set(['3','2'])
        BFS('0', nodeHash, visitor, [])
        self.assertEqual(
            visitor.visited,
            ['0', '1', '3', '4', '2', '3', '4']
            )


if __name__ == '__main__':
    unittest.main(verbosity=1)
