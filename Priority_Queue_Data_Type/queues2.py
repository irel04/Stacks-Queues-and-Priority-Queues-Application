from collections import deque
from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self._elements =[]
    
    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def deqeue(self):
        return heappop(self._elements)[1]