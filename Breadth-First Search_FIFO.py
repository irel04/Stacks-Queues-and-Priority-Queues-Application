import networkx as nx
from graph import City, load_graph

# Return year 
def is_twentieth_century(year):
    return year and 1901 <= year <= 2000


print(" ")
# It is necessary to create a sorting function so that the node that will be returned are through consistent process
def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

# Return city that granted city status in twentieth century
nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
else:
    print("Not found")