from nodeFactory import node_hash
from circularity import loop_find

nodeHash = node_hash('directional_data.txt', ignore=[], verbose=True)

loop_find(nodeHash, verbose=True)
