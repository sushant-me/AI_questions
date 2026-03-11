"""
Implement multiprocessing.
"""

from multiprocessing import Pool

def worker_function(x):
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        results = pool.map(worker_function, range(10))
    print(results)