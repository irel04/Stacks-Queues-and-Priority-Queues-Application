# Importing a module
from collections import deque

class Queue:
    def __init__(self, *elements):
        self.__elements = deque(elements)

    def __len__(self):
        return len(self.__elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self.__elements.append(element)
    
    def dequeue(self):
        return self.__elements.popleft()

# Creating a class STACK
class Stack(Queue):
    def dequeue(self):
        return self.__elements.pop()
