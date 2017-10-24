import csv

links_hash = {}
firstLine = True
with open('directional_data.txt', 'r') as tsv:
    for line in csv.reader(tsv, delimiter=";"):
        if firstLine:
            firstLine = False
            continue
        if len(line) != 4:
            print("ERROR: ")
            print(line)
            continue
        path, eachline, pythonifiedpath, importedmodule = line
        if links_hash.get(pythonifiedpath) is None: links_hash[pythonifiedpath] = set()
        links_hash[pythonifiedpath].add(importedmodule)

print(links_hash)
print(len(links_hash))

def DFS(node, visit, path):
    for eachNode in links_hash[node]:
        newPath = path + [node]
        if links_hash.get(eachNode) is not None:
            DFS(eachNode, visit, newPath)
        else:
            [visited_nodes.add(n) for n in path]
    visit(node, path)

global visited_nodes
visited_nodes = set()

def _loop_find(node, path):
    if node in path[:-1]:
        print("Found a loop!")
        print(path)
        [visited_nodes.add(n) for n in path]

def loop_find(node):
    path = [node]
    DFS(node, _loop_find, path)

print("\n\nBegin!")
for eachNode in links_hash.keys():
    if eachNode not in visited_nodes:
        loop_find(eachNode)
print("Done!")
