from traversal import BFS


class LoopFindVisitor(object):
    def __init__(self):
        self.visitedNodes = set()
        self.loops = []

    def visit(self, node, path):
        self.visitedNodes.add(node)
        if node in path[:-1]:
            self.loops.append(loop_for(path, node))
            return True

    def node_visited(self, node):
        return node in self.visitedNodes


def find_loops(nodeHash, verbose=False):
    if verbose is True: print("\nBegin!")
    loopsVisitor = LoopFindVisitor()
    for eachNode in nodeHash.keys():
        if not loopsVisitor.node_visited(eachNode):
            BFS(eachNode, nodeHash, loopsVisitor, [])
    if verbose is True:
        if len(loopsVisitor.loops) > 0:
            print("Loops: ")
        else:
            print("No loops found!")
        for l in loopsVisitor.loops:
            print(l)
        print("Done!")
    return loopsVisitor.loops


def loop_for(path, node):
    loopStart = path.index(node)
    return tuple(path[loopStart:])


def group_loops_by_module(loops, verbose=False):
    problemModules = {}
    for eachLoop in loops:
        for eachModule in eachLoop:
            if problemModules.get(eachModule) is None:
                problemModules[eachModule] = set()
            problemModules[eachModule].add(eachLoop)
    for eachModule in problemModules.keys():
        if len(problemModules.get(eachModule)) == 1:
            del problemModules[eachModule]
    if verbose is True:
        print("problemModules: ", problemModules)
    return problemModules
