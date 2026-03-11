"""
Synchronize threads using locks.
"""

import threading

def worker(lock, thread_id):
    lock.acquire()
    try:
        print(f"Thread {thread_id} is working")
    finally:
        lock.release()

if __name__ == "__main__":
    lock = threading.Lock()
    threads = []
    
    for i in range(5):
        thread = threading.Thread(target=worker, args=(lock, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()