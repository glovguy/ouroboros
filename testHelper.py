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

class GitMock(object):
    @classmethod
    def set_ls_files(cls, ls_files):
        cls.files = ls_files

    def ls_files(self):
        return self.files