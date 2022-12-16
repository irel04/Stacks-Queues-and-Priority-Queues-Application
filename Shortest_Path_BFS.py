import networkx as nx
from graph import City, load_graph

# instantiating nodes and graphs
nodes, graph = load_graph("roadmap.dot", City.from_dict)
