from tabulate import tabulate
from circularity.group import group_loops_by_module


SORT_BY_MODULE = lambda pair: pair[1]


def display_problem_modules(loops):
    problemModules = group_loops_by_module(loops, verbose=False)
    problemModuleStats = [[mod, len(problemModules[mod])] for mod in problemModules]
    problemModuleStats = sorted(problemModuleStats, key=SORT_BY_MODULE, reverse=True)
    print(tabulate(problemModuleStats, headers=['Module', '# of loops']))
