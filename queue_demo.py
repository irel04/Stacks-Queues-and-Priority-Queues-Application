from queues import Queue

fifo = Queue("1st", "2nd", "3rd", "4th", "5th")
print(len(fifo))

for data in fifo:
    print(data)

