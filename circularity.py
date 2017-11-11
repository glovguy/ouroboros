from traversal import BFS
from tqdm import tqdm


class LoopFindVisitor(object):
    def __init__(self):
        self.visitedNodes = set()
        self.loops = set()

    def visit(self, node, path):
        if node in path[:-1]:
            self.loops.add(loop_for(path, node))
            return True
        if self.node_visited(node):
            return True
        self.visitedNodes.add(node)

    def node_visited(self, node):
        return node in self.visitedNodes


def find_loops(nodeHash, verbose=False):
    if verbose is True: print("\nBegin!")
    loopsVisitor = LoopFindVisitor()
    nodes = nodeHash.keys()
    if verbose is True:
        nodes = tqdm(nodes)
    for eachNode in nodes:
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
    for eachModule in list(problemModules.keys()):
        if len(problemModules.get(eachModule)) == 1:
            del problemModules[eachModule]
    if verbose is True:
        print("problemModules: ", problemModules)
    return problemModules


def get_edges_from_loops(*loops):
    for loop in loops:
        for i in range(0, len(loop)-1):
            yield (loop[i], loop[i+1])
        yield (loop[-1], loop[0])


def edges_from_loops(loops):
    edgeGen = get_edges_from_loops(*loops)
    return [x for x in edgeGen]
