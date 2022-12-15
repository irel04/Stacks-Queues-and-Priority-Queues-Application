from typing import NamedTuple

# Class for City 
class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float