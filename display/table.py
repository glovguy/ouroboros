from tabulate import tabulate
from circularity import group_loops_by_module


def display_problem_modules(loops):
    problemModules = group_loops_by_module(loops, verbose=False)
    problemModuleStats = sorted([[mod, len(problemModules[mod])] for mod in problemModules], key=lambda pair: pair[1])
    print tabulate(problemModuleStats, headers=['Module', '# of loops'])
