import multiprocessing
import requests
import time
import tracemalloc
import psutil
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def fetch(url):
    logging.info(f"Fetching {url}")
    response = requests.get(url)
    return response.text


def multiprocessing_main(urls):
    num_processes = min(50, len(urls))
    logging.info(f"Starting multiprocessing with {num_processes} processes")

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(fetch, urls)
    return results


def profile_multiprocessing():
    urls = ["https://www.examples.com"] * 100


    tracemalloc.start()

    start_time = time.time()
    results = multiprocessing_main(urls)
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)


    logging.info(f"Multiprocessing I/O time: {end_time - start_time:.2f} seconds")
    logging.info(f"Memory usage: {mem_usage:.2f} MB")


if __name__ == '__main__':
    profile_multiprocessing()