
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
