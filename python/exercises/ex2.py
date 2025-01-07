# 2. Threading: Producător și Consumator (Listă limitată)
# Extinde conceptul producător-consumator:

# Creează o listă partajată cu o dimensiune maximă de 10 elemente.
# Producătorul adaugă valori în listă, dar trebuie să aștepte dacă lista este plină.
# Consumatorul scoate valori din listă și așteaptă dacă lista este goală.
# Folosește threading.Condition pentru sincronizare.

import threading
from queue import Queue
from time import sleep

buffer = Queue(5)
condition = threading.Condition()

def producer():
    elements = range(0, 20)
    
    for el in elements:
        with condition:
            while buffer.qsize() > 4:
                print("buffer is full... waiting")
                condition.wait()

            print("Producer produced ", el)
            buffer.put(el)
            condition.notify_all()
        sleep(0.1)
        
    with condition:
            while buffer.qsize() > 4:
                print("buffer is full... waiting")
                condition.wait()

            print("Producer produced END")
            buffer.put("END")
            condition.notify_all()
    sleep(0.1)

def consumer():
    msg = None 
    while msg != "END":
        with condition:
            while buffer.qsize() == 0:
                print("buffer is empty... waiting")
                condition.wait()
            
            msg = buffer.get()
            print("Consumer consumed ", msg)

            condition.notify_all()
        sleep(0.5)


if __name__ == '__main__':
    pt = threading.Thread(target=producer, args=[])
    ct = threading.Thread(target=consumer, args=[])

    pt.start()
    ct.start()

    pt.join()
    ct.join()
    

