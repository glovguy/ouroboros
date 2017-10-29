
class MockVisitor(object):
        def __init__(self):
            self.visited = []

        def visit(self, node, path):
            self.visited.append(node)
