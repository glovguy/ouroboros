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
