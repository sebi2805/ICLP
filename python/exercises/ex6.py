# 8. Paralelizare: Sortare cu Divide and Conquer
# Extinde ideea sortării paralele:

# Implementă o sortare prin "Merge Sort" folosind multiprocessing.
# Împarte lista în părți mai mici, procesele sortează fiecare sublistă, iar lista finală este combinată de procesul principal.


import threading
import random
from time import sleep

# Contor global
counter = 0
counter_lock = threading.Lock()

# Eveniment pentru a semnaliza start-ul
start_event = threading.Event()

def increment_thread(thread_id):
    global counter
    while True:
        # Așteptăm semnalul de start
        start_event.wait()

        # Incrementăm contorul cu blocare
        with counter_lock:
            if counter >= 100:
                break  # Ieșim dacă contorul a atins 100
            increment = random.randint(1, 10)
            counter += increment
            print(f"Thread {thread_id} incremented by {increment}, counter is now {counter}")

        # Pauză scurtă pentru a simula activitate
        sleep(random.random())

if __name__ == "__main__":
    # Creăm și pornim 3 thread-uri
    threads = []
    for i in range(3):
        t = threading.Thread(target=increment_thread, args=(i,))
        threads.append(t)
        t.start()

    # Semnalizăm start-ul după o pauză
    print("Main thread is ready. Starting increment threads...")
    sleep(1)
    start_event.set()

    # Așteptăm ca toate thread-urile să se încheie
    for t in threads:
        t.join()

    print(f"Final counter value: {counter}")
