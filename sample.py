# from generate import number_queue, number_queue2, generate_random_number
# import threading
# import queue

# def printa():
#     while True:
#         try:
#             a = number_queue.get(timeout= 3)
#             b = number_queue2.get(timeout= 3)
#             print(a)
#             print(b)

#         except queue.Empty:
#             pass   #Handle case if queue is empty


# t1 = threading.Thread(target=generate_random_number)
# t1.start()

# t2 = threading.Thread(target=printa)
# t2.start()

values = ("Fetching", "Fetching")
print(values[1])