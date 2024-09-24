import asyncio
import time
import tracemalloc
import psutil


def blocking_task(i):
    time.sleep(0.1)
    return i



async def async_main():
    loop = asyncio.get_event_loop()

    tasks = [loop.run_in_executor(None, blocking_task, i) for i in range(1000)]
    return await asyncio.gather(*tasks)



def profile_asyncio_parallelism():
    tracemalloc.start()

    start_time = time.time()
    asyncio.run(async_main())
    end_time = time.time()

    process = psutil.Process()
    mem_usage = process.memory_info().rss / (1024 * 1024)
    print("Asyncio (blocking) parallelism time:", end_time - start_time)
    print(f"Memory usage: {mem_usage:.2f} MB")


profile_asyncio_parallelism()