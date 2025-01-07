import threading
import multiprocessing
from queue import Queue
from time import sleep
from time import perf_counter
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    with ThreadPoolExecutor(4) as pool:
        futures ={ pool.submit(factorial, i):i for i in range(1, 21)}

        for future in as_completed(futures):
            print(futures[future], future.result())