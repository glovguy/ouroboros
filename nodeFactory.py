import re
import csv


def pythonify_path(path):
    p = re.sub(r'.*(/).*', '.', path)
    return re.sub(r'\.py', '', p)


def node_hash(fileName, verbose=False):
    nodeHash = {}
    firstLine = True
    with open(fileName, 'r') as tsv:
        for line in csv.reader(tsv, delimiter=";"):
            if firstLine:
                firstLine = False
                continue
            if len(line) != 3 and verbose is True:
                print("ERROR: ")
                print(line)
                continue
            path, eachline, importedmodule = line
            pythonifiedPath = pythonify_path(path)
            if nodeHash.get(pythonifiedPath) is None: nodeHash[pythonifiedPath] = set()
            nodeHash[pythonifiedPath].add(importedmodule)
    if verbose is True:
        print("nodeHash: ")
        print(nodeHash)
        print("Length: ")
        print(len(nodeHash))
    return nodeHash
