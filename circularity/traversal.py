
def BFS(node, nodeHash, visitor, path):
    if visitor.visit(node, path): return
    for eachChild in sorted(list(nodeHash[node])):
        newPath = path + [node]
        if nodeHash.get(eachChild) is not None:
            BFS(eachChild, nodeHash, visitor, newPath)


def BFS_with_stack(stack, nodeHash, visit, visited, tally):
    while len(stack) > 0:
        nextNode, nextPath = stack.pop()
        while nodeHash.get(nextNode) is None:
            if len(stack) == 0: return tally
            nextNode, nextPath = stack.pop()
        if visit(nextNode, nextPath, tally, visited): continue
        for eachChild in nodeHash[nextNode]:
            stack.append((eachChild, nextPath + [nextNode]))
    return tally
