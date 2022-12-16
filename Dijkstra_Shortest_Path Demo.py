import networkx as nx
from graph import City, load_graph, dijkstra_shortest_path

nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["london"]
city2 = nodes["edinburgh"]

def distance(weights):
    return float(weights["distance"])

print("\n\nWeight-Distance sort Approach:")
for city in dijkstra_shortest_path(graph, city1, city2, distance):
    print(city.name)

print("\n\nWeight sort Approach:")
def weight(node1, node2, weights):
    return distance(weights)

for city in nx.dijkstra_path(graph, city1, city2, weight):
    print(city.name)