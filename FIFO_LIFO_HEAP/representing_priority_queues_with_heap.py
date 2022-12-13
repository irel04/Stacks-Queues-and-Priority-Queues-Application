# Importing the module
from heapq import heappush
fruits = []
print("\nUsing Heappop")
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

from heapq import heappop
print("\nUsing Heappop")
print("item remove:", heappop(fruits))
print(fruits)