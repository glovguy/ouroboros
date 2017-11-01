import re
import csv


def node_hash(fileName, ignore=[], verbose=False):
    with open(fileName, 'r') as directionalData:
        csvFile = csv.reader(directionalData, delimiter=";")
        next(csvFile)  # Skip header
        nodeHash = hash_from_csv(csvFile, ignore)
    if verbose is True: print("nodeHash: ", nodeHash, "Length: ", len(nodeHash))
    return nodeHash


def hash_from_csv(csvFile, ignore):
    nodeHash = {}
    for line in csvFile:
        path, eachline = line
        pythonifiedPath = pythonify_path(path)
        if ignore_node(pythonifiedPath, ignore): continue
        if nodeHash.get(pythonifiedPath) is None:
            nodeHash[pythonifiedPath] = set()
        nodeHash[pythonifiedPath].add(imported_module(eachline))
    return nodeHash


def pythonify_path(path):
    p = re.sub(r'/', '.', path)
    return re.sub(r'\.py', '', p)


def imported_module(line):
    import_partial_module = re.search(r'.*from.*', line)
    if import_partial_module is not None:
        return re.search(r'from (.*) import.*', line).group(1)
    import_whole_module = re.search(r'import (.*)', line)
    if import_whole_module:
        return import_whole_module.group(1)
    return None


def ignore_node(node, ignore):
    for eachPattern in ignore:
        if re.search(eachPattern, node) is not None: return True
    return False
