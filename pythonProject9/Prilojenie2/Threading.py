import threading
import time
import tracemalloc
import psutil


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def threaded_fibonacci(n, results, index):
    results[index] = fibonacci(n)


def threaded_main():
    numbers = [30, 32, 34]
    results = [None] * len(numbers)
    threads = []

    for i, number in enumerate(numbers):
        thread = threading.Thread(target=threaded_fibonacci,
                                  args=(number, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading_computation():

    tracemalloc.start()

    start_time = time.time()
    threaded_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)
    print("Threading computation time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading_computation()
