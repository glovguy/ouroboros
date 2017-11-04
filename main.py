from nodeFactory import node_hash
from circularity import find_loops
from display.graph import display_loops
from display.table import display_problem_modules

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=False)
loops = find_loops(nodeHash, verbose=False)


def save_loops(loops, fileName='loops.txt'):
    with open(fileName) as loopsFile:
        for loop in loops:
            loopsFile.write("%s\n" % str(loop))


def load_loops(fileName):
    loops = set()
    with open(fileName) as loopsFile:
        for line in loopsFile:
            loops.add(line)
    return loops


display_problem_modules(loops)
display_loops(loops)
