
def BFS(node, nodeHash, visitor, path):
    if visitor.visit(node, path): return
    for eachChild in sorted(list(nodeHash[node])):
        newPath = path + [node]
        if nodeHash.get(eachChild) is not None:
            BFS(eachChild, nodeHash, visitor, newPath)
