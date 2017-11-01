from nodeFactory import node_hash
from circularity import find_loops
from display.graph import display_loops
from display.table import display_problem_modules

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=False)
loops = find_loops(nodeHash, verbose=False)

display_problem_modules(loops)
display_loops(loops)
