from circularity import LoopFindVisitor

class setMock(list):
    def add(self, el):
        self.append(el)

class MockVisitor(object):
        def __init__(self):
            self.visited = []

        def visit(self, node, path):
            self.visited.append(node)

class MockLoopFindVisitor(LoopFindVisitor):
    def __init__(self):
        self.visitedNodes = set()
        self.loops = setMock()

def mock_visit(node, path, loops, visited):
    from circularity import loop_for
    if isinstance(visited, set):
        visited = list(visited)
    if node in path[:-1]:
        loops.add(loop_for(path, node))
        return True
    if node in visited:
        return True
    visited.append(node)

class GitMock(object):
    @classmethod
    def set_ls_files(cls, ls_files):
        cls.files = ls_files

    def ls_files(self):
        return self.files

mockFile = """
import main
from first import second
def function():
    pass
# Some comment with the word import in it
""".split("\n")