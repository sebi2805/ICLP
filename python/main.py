import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import time 
import random 

def clock():
    return time.clock_gettime(time.CLOCK_MONOTONIC)


async def doWork():
    await asyncio.sleep(0.1)
    return random.randint(1, 10)

async def main():
    futures = [asyncio.create_task(doWork()) for _ in range(10)]
    await asyncio.gather(*futures)
    for f in futures:
        print(f.result())

if __name__ == "__main__":            
    asyncio.run(main())