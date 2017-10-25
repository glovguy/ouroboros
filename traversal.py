
def BFS(node, nodeHash, visitor, path):
    if visitor.visit(node, path): return
    for eachNode in nodeHash[node]:
        newPath = path + [node]
        if nodeHash.get(eachNode) is not None:
            BFS(eachNode, nodeHash, visitor, newPath)
