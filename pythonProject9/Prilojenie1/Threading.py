import threading
import requests
import time
import tracemalloc
import psutil


def fetch(url, results, index):
    response = requests.get(url)
    results[index] = response.text


def threaded_main(urls):
    results = [None] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch, args=(url, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def profile_threading():
    urls = ["https://www.examples.com"] * 100


    tracemalloc.start()

    start_time = time.time()
    threaded_main(urls)
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Threading I/O time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_threading()