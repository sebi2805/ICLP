#  Barieră: Sincronizare mai complexă
# Creează 5 thread-uri care simulează mașini ce trebuie să parcurgă 3 puncte de control (bariere).
# Fiecare mașină trebuie să aștepte celelalte la fiecare punct de control înainte de a continua.
# Folosește threading.Barrier pentru a sincroniza.
import threading
import multiprocessing
from queue import Queue
from time import sleep
from time import perf_counter
import random

def car(car_id, barrier):
    for i in range(3):
        t = random.random() * 5
        sleep(t)

        print(f'Car {car_id} is arrived barrier {i} in {t:.02f} secunde')
        barrier.wait()

if __name__ == '__main__':
    cars = []
    barrier = threading.Barrier(5)
    for i in range (5):
        ci = threading.Thread(target=car, args=(i, barrier))
        cars.append(ci)
        ci.start()
    
    for ci in cars:
        ci.join()