import multiprocessing
import time
import tracemalloc
import psutil



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def worker(n, queue):
    result = fibonacci(n)
    queue.put(result)


def multiprocessing_main():
    numbers = [30, 32, 34]
    queue = multiprocessing.Queue()
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=worker, args=(number, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = [queue.get() for _ in range(len(numbers))]
    return results


def profile_multiprocessing_computation():

    tracemalloc.start()

    start_time = time.time()
    multiprocessing_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Multiprocessing computation time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing_computation()