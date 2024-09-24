import threading
import time
import tracemalloc
import psutil


def process_task(i):
    time.sleep(0.1)



def threaded_main():
    threads = []

    for i in range(1000):
        thread = threading.Thread(target=process_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading_parallelism():
    tracemalloc.start()

    start_time = time.time()
    threaded_main()
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Threading parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading_parallelism()