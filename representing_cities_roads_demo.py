import pygraphviz as pgv
import networkx as nx
from graph import City, load_graph

# Roadmap demo
print(nx.nx_agraph.read_dot("roadmap.dot"))


