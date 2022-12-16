Commands that are necessary to run specific demo:

# For thread-safe queues
thread_safe_queues_PrioQueue.py -> py thread_safe_queues.py --queue lifo
thread_safe_queues_PrioQueues.py -> py thread_safe_queues_PrioQueues.py --queue heap

# For importing Local Server from python run these commands
cd venv/
python -m http.server

# For asynchronous queues
async_queues_LIFO.py -> python async_queues.py http://localhost:8000 --max-depth=4
async_queues.py -> python async_queues.py http://localhost:8000 --max-depth 5
async_queues_PrioQueue.py -> python async_queues.py http://localhost:8000 --max-depth=4


Disclaimer: The codes are from Real Python community who offers tutorial. It was used for educational purpose only in compliance of school exercises and demo with QUEUES

link:   https://realpython.com/queue-in-python/#learning-about-the-types-of-queues
