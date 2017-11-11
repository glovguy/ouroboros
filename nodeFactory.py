import re
import csv
from tqdm import tqdm
from project_imports import *


def node_hash_from_csv(fileName, ignore=[], verbose=False):
    with open(fileName, 'r') as directionalData:
        csvFile = csv.reader(directionalData, delimiter=";")
        next(csvFile)  # Skip header
        csvFile = tqdm(csvFile)
        nodeHash = hash_from_iterator(csvFile, ignore)
    if verbose is True: print("nodeHash: ", nodeHash, "Length: ", len(nodeHash))
    return nodeHash


def node_hash_from_file_names(fileNameList):
    nodeHash = {}
    for eachFileName in fileNameList:
        with open(eachFileName) as file:
            importedModules = imported_modules(file)
            add_node_to_hash(nodeHash, eachFileName, importedModules)
    return nodeHash


def add_node_to_hash(nodeHash, node, importedModules, ignore=[]):
    if not isinstance(importedModules, set):
        importedModules = set([importedModules])
    nodeName = pythonify_path(node)
    if ignore_node(nodeName, ignore):
        return nodeHash
    if nodeHash.get(nodeName) is None:
        nodeHash[nodeName] = set()
    nodeHash[nodeName] = nodeHash[nodeName].union(importedModules)
    return nodeHash


def hash_from_iterator(iterator, ignore=[]):
    nodeHash = {}
    for line in iterator:
        path, eachline = line
        import_name = imported_module_name(eachline)
        add_node_to_hash(nodeHash, path, import_name)
    return nodeHash


def pythonify_path(path):
    p = re.sub(r'/', '.', path)
    return re.sub(r'\.py', '', p)


def ignore_node(node, ignore):
    for eachPattern in ignore:
        if re.search(eachPattern, node) is not None: return True
    return False
