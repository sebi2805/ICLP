import threading

barrier = threading.Barrier(3)  # 3 fire trebuie să atingă bariera

def task(n):
    print(f"Firul {n} ajunge la barieră")
    barrier.wait()
    print(f"Firul {n} continuă")

threads = [threading.Thread(target=task, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()
