import networkx as nx

# X=nx.DiGraph()
# edges=[(1, 2), (2, 6), (1, 7), (3, 1), (6, 5), (4, 5), (2, 8), (5, 2), (3, 2), (4, 7), (1, 8)]
# X.add_edges_from(edges)
# print(X.nodes)

# Y = nx.fast_gnp_random_graph(12, 0.314[directed])
# for x in Y.nodes:
#     for y in Y.nodes:
# X=nx.scale_free_graph(12)
# X=nx.gn_graph(12)

# print(X.nodes)
# print(X.edges)

while len(X.edges)>0:
    for ponto in nx.isolates(X):
        X.remove_node(ponto)
    print(X.nodes)
    print(X.edges)
    seta0 = input("selecione uma seta ")
    if (int(seta0[0]), int(seta0[0])) in X.edges:
        ponto=int(seta0[2])
        X.remove_nodes_from(nx.descendants(X, ponto))
        X.remove_node(ponto)

