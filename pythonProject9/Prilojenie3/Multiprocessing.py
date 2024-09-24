import multiprocessing
import time
import tracemalloc
import psutil


def process_task(i):
    time.sleep(0.1)


def multiprocessing_main():
    processes = []

    for i in range(1000):
        process = multiprocessing.Process(target=process_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def profile_multiprocessing_parallelism():
    tracemalloc.start()

    start_time = time.time()
    multiprocessing_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)
    print("Multiprocessing parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing_parallelism()