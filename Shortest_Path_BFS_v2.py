import networkx as nx
from graph import City, load_graph, shortest_path, connected
# instantiating nodes and graphs
nodes, graph = load_graph("roadmap.dot", City.from_dict)

city1 = nodes["aberdeen"]
city2 = nodes["perth"]

print(" ")
# Implementing shortest path with Queue class
print(" → ".join(city.name for city in shortest_path(graph, city1, city2)))

# Shortest path by latitude 
def by_latitude(city):
    return -city.latitude


print("\n\nShortest path latitude: ")
print(" → ".join(
    city.name
    for city in shortest_path(graph, city1, city2, by_latitude)
))

print("\nDetermining if two nodes are connected:")
# This line of code will only execute a boolean value because it only determine if the city are connected 
print("Belfast and Glasgow are connected: ", connected(graph, nodes["belfast"], nodes["glasgow"]))
print("Belfast and Derry are connected: ", connected(graph, nodes["belfast"], nodes["derry"]))