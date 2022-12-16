import pygraphviz as pgv
import networkx as nx
from graph import City, load_graph

# Roadmap demo
print("\n\nDemo: Summary Information")
print(nx.nx_agraph.read_dot("roadmap.dot"))

# Viewing imported CLASS
print("\n\nDemo: Graph Nodes")
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])

# printing the nodes and graph using load_graph method for creating instances
print("\n\nDemo: Nodes and graph")
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(nodes["london"])
print(graph)

# Printing Neighbors using the neighbor method
print("\n\nDemo: Printing Neighbors")
for neighbor in graph.neighbors(nodes["london"]):
    print(neighbor.name)

# Neighbors + weights
print("\n\nDemo: Printing Neighbors + Weights")
for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)


# Sorting by distance using defined functions
print("\n\nDemo: Sorting by distancegit")
def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")

