from queues import PriorityQueue
from dataclasses import dataclass

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

@dataclass
class Message:
     event: str

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")


print("\n")
print(messages.dequeue())


