import concurrent.futures

def worker(task):
    """Worker function to process a task."""
    # Simulate task processing
    print(f"Processing task: {task}")
    return f"Result of {task}"

def create_thread_pool(num_threads):
    """Create a thread pool and execute tasks."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        tasks = [f"Task-{i}" for i in range(5)]
        results = list(executor.map(worker, tasks))
    return results

# Example usage
if __name__ == "__main__":
    results = create_thread_pool(3)
    print("All tasks completed:", results)