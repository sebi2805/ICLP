import threading

rlock = threading.RLock()

def recursive_function(n):
    with rlock:
        if n > 0:
            print(f"Recursivitate: {n}")
            recursive_function(n - 1)

thread = threading.Thread(target=recursive_function, args=(5,))
thread.start()
thread.join()
