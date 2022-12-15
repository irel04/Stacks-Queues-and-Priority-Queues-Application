import networkz as nx
print(nx.nx_agraph.read_dot("roadmap.dot"))
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]