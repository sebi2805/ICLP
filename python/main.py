# Problema 1. 
# Fie un array de numere. Sa se scrie un algoritm paralel de sortare a acestor numere. \

from concurrent.futures import ThreadPoolExecutor
import threading 
import time 
import numpy as np
import random 

def clock():
    return time.clock_gettime(time.CLOCK_MONOTONIC)


def consumer(left, right):
    result = [] 
    i = j = 0 
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1 
        else:
            result.append(right[j])
            j += 1 
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result 




class Producer():
  def __init__(self):
    self.arr = random.choices(range(1000), k=100)
    self.sorted_arr = []

    self.num_workers = 4
    self.consumers = [Consumer(self.arr) for _ in range(self.num_workers)]

  def produce(self):
    self.sorted_arr = []

  def merge_sort(self):
      if len(self.arr) <= 1: 
          return self.arr 
          
      mid = len(self.arr) // 2 
      left = self.arr[:mid]
      right = self.arr[mid:]

      result = threading.Thread(target=consumer, args=(left,right))
      
      result.start()

      try:
          result.join()
          result.
      except:
          print("It did throw an error ")
          pass

      return self.merge(left, right)

if __name__ == "__main__":
    arr = random.choices(range(1000), k=100)
    start_time = clock()
    end_time = clock()
    print(f"Time: {end_time - start_time}")