from graph import (
    City,
    load_graph,
    breadth_first_traverse,
    breadth_first_search as bfs,
)

# Function that return year of a city
def is_twentieth_century(city):
    return city.year and 1901 <= city.year <= 2000

# This is where the implementation of bread_first_search 
nodes, graph = load_graph("roadmap.dot", City.from_dict)
city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
city.name

# Searching through loops
for city in breadth_first_traverse(graph, nodes["edinburgh"]):
    print(city.name)