import unittest
from testHelper import *
from nodeFactory import *
import circularity
from traversal import *
import project_imports


class test_project_imports(unittest.TestCase):
    def test_all_project_python_files(self):
        GitMock.set_ls_files(
            'fileOne.py\nfileTwo.py\nnon_python_file.sh\nfolder/file_in_folder.py\nfolder/markdown.md')
        project_imports.Git = GitMock
        self.assertEqual(
            project_imports.all_project_python_files(),
            ['fileOne.py', 'fileTwo.py', 'folder/file_in_folder.py']
            )

    def test_imported_module_name_form_1(self):
        self.assertEqual(
            project_imports.imported_module_name('from user import contacts'),
            'user'
            )

    def test_imported_module_name_form_2(self):
        self.assertEqual(
            project_imports.imported_module_name('import contacts'),
            'contacts'
            )

    def test_remove_comments(self):
        self.assertEqual(
            remove_comments("function()# Some comment"),
            "function()"
            )

    def test_imported_modules(self):
        self.assertEqual(
            imported_modules(mockFile),
            set(['main', 'first'])
            )


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
            hash_from_iterator([['file', 'import other_file']]),
            { 'file': set(['other_file']) }
            )

    def test_add_node_to_hash(self):
        self.assertEqual(
            add_node_to_hash({}, 'node_name', 'imported_module'),
            {'node_name': set(['imported_module'])}
            )


class test_circularity(unittest.TestCase):
    def test_loop_find_visitor_keeps_track_of_visited_nodes(self):
        visitor = circularity.LoopFindVisitor()
        visitor.visit('nodename', [])
        self.assertTrue(visitor.node_visited('nodename'))

    def test_loop_find_visitor_identifies_loop(self):
        visitor = circularity.LoopFindVisitor()
        self.assertTrue(visitor.visit('n3', ['n1', 'n2', 'n3', 'n4']))
        self.assertEqual(visitor.loops, set([('n3', 'n4')]))

    def test_loop_find_visitor_does_not_identify_non_loop(self):
        visitor = circularity.LoopFindVisitor()
        self.assertNotEqual(visitor.visit('n3', ['n1', 'n2']), True)

    def test_loop_for(self):
        path = ['n1', 'n2', 'n3', 'n4']
        self.assertEqual(
            circularity.loop_for(path, 'n3'),
            ('n3', 'n4')
            )

    def test_find_loops(self):
        loops = circularity.find_loops({'n1': set(['n2']), 'n2': set(['n3']), 'n3': set(['n1'])})
        self.assertEqual(len(loops), 1)
        self.assertEqual(loops, set([('n1', 'n2', 'n3')]))

    def test_find_loops_is_efficient(self):
        _LoopFindVisitor = circularity.LoopFindVisitor
        circularity.LoopFindVisitor = MockLoopFindVisitor
        loops = circularity.find_loops(
            {'n1': set(['n2']),
            'n2': set(['n3']),
            'n3': set(['n1']),
            'n5': set(['n1']),
            'n6': set(['n2']),
            'n7': set(['n3'])
            })
        self.assertEqual(len(loops), len(set(loops)))
        circularity.LoopFindVisitor = _LoopFindVisitor

    def test_find_loops_with_stack(self):
        loops = circularity.find_loops_with_stack({'n1': set(['n2']), 'n2': set(['n3']), 'n3': set(['n1'])})
        self.assertEqual(len(loops), 1)
        self.assertEqual(loops, set([('n1', 'n2', 'n3')]))

    def test_find_loops_with_stack_is_efficient(self):
        _visit = circularity.visit
        circularity.visit = mock_visit
        loops = circularity.find_loops_with_stack(
            {'n1': set(['n2']),
            'n2': set(['n3']),
            'n3': set(['n1']),
            'n5': set(['n1']),
            'n6': set(['n2']),
            'n7': set(['n3'])
            })
        self.assertEqual(len(loops), len(set(loops)))
        circularity.visit = _visit

    def test_group_loops_by_module(self):
        loops = [
            ('1', '2'),
            ('3', '4'),
            ('1', '5', '6'),
            ('4', '7')
            ]
        groups = circularity.group_loops_by_module(loops)
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
        self.assertEqual(circularity.edges_from_loops(loops), expectedEdges)


class test_traversal(unittest.TestCase):
    def test_breadth_first_search_visits_all_nodes_in_depth_first_order(self):
        visitor = MockVisitor()
        maxN = 3
        nodeHash = {str(x): str(x+1) for x in range(0, maxN)}
        nodeHash['0'] = set(['1','4'])
        nodeHash['4'] = set(['5'])
        nodeHash['5'] = set(['6'])
        BFS('0', nodeHash, visitor, [])
        self.assertEqual(
            visitor.visited,
            ['0', '1', '2', '4', '5']
            )


if __name__ == '__main__':
    unittest.main(verbosity=1)
