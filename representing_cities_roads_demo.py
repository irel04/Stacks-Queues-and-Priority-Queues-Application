import pygraphviz as pgv
import networkx as nx
from graph import City, load_graph

# Roadmap demo
print("\n", nx.nx_agraph.read_dot("roadmap.dot"))

# Viewing imported CLASS
graph = nx.nx_agraph.read_dot("roadmap.dot")
print("\n\n", graph.nodes["london"])

