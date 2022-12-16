import networkx as nx
from graph import City, load_graph, shortest_path

# instantiating nodes and graphs
nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

print(" ")
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))