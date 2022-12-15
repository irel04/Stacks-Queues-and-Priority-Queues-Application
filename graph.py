from typing import NamedTuple

# Class for City 
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    # For storing data in dict
    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )
    
    # A graph instance that take note of the mapping of node identifiers to city instances
    def load_graph(filename, node_factory):
        graph = nx.nx_agraph.read_dot(filename)
        nodes = {
            name: node_factory(attributes)
            for name, attributes in graph.nodes(data=True)
        }
        return nodes, nx.Graph(
            (nodes[name1], nodes[name2], weights)
            for name1, name2, weights in graph.edges(data=True)
    )