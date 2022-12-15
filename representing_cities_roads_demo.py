import networkz as nx
from graph import City, load_graph

# Roadmap demo
print(nx.nx_agraph.read_dot("roadmap.dot"))
graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]

# Using Class -> City() and Method -> load_graph from the graph.py module
nodes, graph = load_graph("roadmap.dot", City.from_dict)

nodes["london"]
print(graph)