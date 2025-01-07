import threading
from queue import Queue
from time import sleep
import random

read_lock = threading.Condition()
count_lock = threading.Lock()
count = 0
BUFFER_SIZE = 5
buffer = Queue(BUFFER_SIZE)

def reader(i):
    global count
    while True:
        with read_lock:
            while buffer.qsize() == 0:  # Așteaptă dacă buffer-ul e gol
                read_lock.wait()
            
            msg = buffer.get()
            print(f'Consumerul {i} a citit: {msg}')
            sleep(0.75)

        # Decrementarea count nu are nevoie de blocare complexă aici
        with count_lock:
            count -= 1
            if count == 0:
                with read_lock:
                    read_lock.notify_all()  # Notifică writerii

def writer(i):
    while True:
        msg = f'Mesajul de writerul {i} cu {random.randint(1, 10)}'
        with read_lock:
            while buffer.qsize() >= BUFFER_SIZE:  # Așteaptă dacă buffer-ul e plin
                read_lock.wait()
            
            buffer.put(msg)
            print(f'Writerul {i} a scris: {msg}')
            sleep(0.5)

            read_lock.notify_all()  # Notifică readerii


if __name__ == '__main__':
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    for w in writers:
        w.start()

    for r in readers:
        r.start()

    for w in writers:
        w.join()

    for r in readers:
        r.join()
