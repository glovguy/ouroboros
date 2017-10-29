from nodeFactory import node_hash
from circularity import find_loops, group_loops_by_module

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=True)

loops = find_loops(nodeHash, verbose=True)

problemModules = group_loops_by_module(loops, verbose=True)
