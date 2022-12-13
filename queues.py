# Importing a module
from collections import deque

class Queue:
    def __init__(self):
        self.__elements = deque()
    
    def enqueue(self, element):
        self.__elements.append(element)
    
    def dequeue(self):
        return self.__elements.popleft()
