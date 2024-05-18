import random
import time
from queue import Queue

#create a queue to store random number
number_queue = Queue()
number_queue2 = Queue()

def generate_random_number():
    while True:
        a = random.randint(3, 45)
        b = time.time()
        number_queue.put(a)
        number_queue2.put(b)
        time.sleep(1)