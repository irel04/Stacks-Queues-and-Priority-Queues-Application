from collections import deque
from heapq import heappop, heappush
from itertools import count

class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()