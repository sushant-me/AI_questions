""" Implement multithreading. """

import threading
import time

def worker(num):
    """Thread worker function"""
    print(f'Worker: {num}')
    time.sleep(2)
    print(f'Worker {num} finished')

threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads completed")