import threading
import time

semaphore = threading.Semaphore(3)  # Permite maxim 3 fire simultan

def task(n):
    with semaphore:
        print(f"Firul {n} rulează")
        time.sleep(2)

threads = [threading.Thread(target=task, args=(i,)) for i in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
