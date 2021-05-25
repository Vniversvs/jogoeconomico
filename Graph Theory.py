import networkx as nx
import matplotlib.pyplot as at

pontos = [1,2,3,4]
elos = [[1, 2], [3, 4]]

X = nx.Graph()

X.add_nodes_from(pontos)
X.add_edges_from(elos)

nx.draw_circular(X)
at.show()
