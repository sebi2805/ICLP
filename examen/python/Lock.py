import threading

lock = threading.Lock()

def critical_section():
    with lock:
        print("Thread-ul accesează secțiunea critică")

threads = [threading.Thread(target=critical_section) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
