# Problema 1. 
# Fie un array de numere. Sa se scrie un algoritm paralel de sortare a acestor numere. \

from concurrent.futures import ThreadPoolExecutor
import threading 
import time 
import numpy as np
import random 

def clock():
    return time.clock_gettime(time.CLOCK_MONOTONIC)

def merge(left, right):
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

def merge_sort(arr):
    if len(arr) <= 1: 
        return arr 
        
    mid = len(arr) // 2 
    left = arr[:mid]
    right = arr[mid:]
    
    with ThreadPoolExecutor() as executor:
        left_sorted = executor.submit(merge_sort, left)
        right_sorted = executor.submit(merge_sort, right)
        
        left = left_sorted.result()
        right = right_sorted.result() 
    
    return merge(left, right)
    
if __name__ == "__main__":
    arr = random.choices(range(1000), k=100)
    start_time = clock()
    sorted_arr = merge_sort(arr)
    end_time = clock()
    print(f"Time: {end_time - start_time}")
    print(sorted_arr)