import threading

event = threading.Event()

def wait_for_event():
    print("Aștept semnalul...")
    event.wait()
    print("Semnal primit!")

def send_event():
    print("Trimit semnal...")
    event.set()

t1 = threading.Thread(target=wait_for_event)
t2 = threading.Thread(target=send_event)

t1.start()
t2.start()
t1.join()
t2.join()
