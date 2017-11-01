from nodeFactory import node_hash
from circularity import find_loops, group_loops_by_module
from display.graph import display_loops

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=False)
loops = find_loops(nodeHash, verbose=False)
# problemModules = group_loops_by_module(loops, verbose=True)

display_loops(loops)


