import threading

condition = threading.Condition()
shared_data = []

def producer():
    with condition:
        shared_data.append(1)
        print("Produs un element")
        condition.notify()  # Anunță consumatorul

def consumer():
    with condition:
        while not shared_data:
            condition.wait()  # Așteaptă notificare de la producător
        print("Consum un element:", shared_data.pop())

t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()
t1.join()
t2.join()
