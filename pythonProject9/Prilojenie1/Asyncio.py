import asyncio
import aiohttp
import time
import tracemalloc
import psutil

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def async_main(urls):
    tasks = [fetch(url) for url in urls]
    return await asyncio.gather(*tasks)


def profile_asyncio():
    urls = ["https://www.examples.com"] * 100


    tracemalloc.start()

    start_time = time.time()
    asyncio.run(async_main(urls))
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)

    print("Asyncio I/O time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_asyncio()