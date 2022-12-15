import pygraphviz as pgv
import networkx as nx
from graph import City, load_graph

# Roadmap demo
print("\n", nx.nx_agraph.read_dot("roadmap.dot"))

# Viewing imported CLASS
graph = nx.nx_agraph.read_dot("roadmap.dot")
print("\n\n", graph.nodes["london"])

# printing the nodes and graph using load_graph method for creating instances
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print("\n\n", nodes["london"])
print(graph)