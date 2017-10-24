import csv
import re

def pythonify_path(path):
    p = re.sub(r'.*(/).*', '.', path)
    return re.sub(r'\.py', '', p)

links_hash = {}
firstLine = True
with open('directional_data.txt', 'r') as tsv:
    for line in csv.reader(tsv, delimiter=";"):
        if firstLine:
            firstLine = False
            continue
        if len(line) != 3:
            print("ERROR: ")
            print(line)
            continue
        path, eachline, importedmodule = line
        pythonifiedpath = pythonify_path(path)
        if links_hash.get(pythonifiedpath) is None: links_hash[pythonifiedpath] = set()
        links_hash[pythonifiedpath].add(importedmodule)

print(links_hash)
print(len(links_hash))

global visited_nodes
visited_nodes = set()

def BFS(node, visit, path):
    if visit(node, path): return
    for eachNode in links_hash[node]:
        newPath = path + [node]
        if links_hash.get(eachNode) is not None:
            BFS(eachNode, visit, newPath)
        else:
            [visited_nodes.add(n) for n in path]

def _cease(node, path):
    return node in path[:-1]

def _loop_find(node, path):
    if _cease(node, path):
        print("Found a loop!")
        print(node)
        print(path)
        [visited_nodes.add(n) for n in path]
        return True

def loop_find(node):
    path = []
    BFS(node, _loop_find, path)



print("\n\nBegin!")
for eachNode in links_hash.keys():
    if eachNode not in visited_nodes:
        loop_find(eachNode)
print("Done!")
