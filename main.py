from nodeFactory import node_hash
from circularity import find_loops

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=True)

loops = find_loops(nodeHash, verbose=True)

def group_loops_by_module(loops, verbose=False):
    problemModules = {}
    for eachLoop in loops:
        if problemModules.get(eachLoop[0]) is None: problemModules[eachLoop[0]] = set()
        problemModules[eachLoop[0]].add(eachLoop)
    if verbose is True: print("problemModules: ", problemModules)
    return problemModules

problemModules = group_loops_by_module(loops, verbose=True)
