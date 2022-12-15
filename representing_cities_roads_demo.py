import networkz as nx
from graph import City, load_graph

# Roadmap demo
print(nx.nx_agraph.read_dot("roadmap.dot"))
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]