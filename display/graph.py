import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from circularity.group import edges_from_loops


def display_loops(loops):
    allEdges = edges_from_loops(loops)
    G = nx.DiGraph()
    G.add_edges_from(allEdges)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('Blues'), node_size = 500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=allEdges, edge_color='b', arrows=True)
    plt.show()
