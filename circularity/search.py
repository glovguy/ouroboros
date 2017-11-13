from circularity.traversal import BFS, BFS_with_stack
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


def find_loops_with_stack(nodeHash, verbose=False):
    if verbose is True: print("\nBegin!")
    nodes = nodeHash.keys()
    visited = set()
    loops = set()
    if verbose is True:
        nodes = tqdm(nodes)
    for eachNode in nodes:
        stack = [(eachNode, [])]
        loops.union(BFS_with_stack(stack, nodeHash, visit, visited, loops))
    if verbose is True:
        if len(loops) > 0:
            print("Loops: ")
        else:
            print("No loops found!")
        for l in loops:
            print(l)
        print("Done!")
    return loops


def visit(node, path, loops, visited):
    if node in path[:-1]:
        loops.add(loop_for(path, node))
        return True
    if node in visited:
        return True
    visited.add(node)


def loop_for(path, node):
    loopStart = path.index(node)
    return tuple(path[loopStart:])
