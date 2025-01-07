# 5. Pipe și Mesaje
# Construiește un sistem cu două procese:

# Procesul "Sender" trimite un mesaj aleatoriu printr-un Pipe la fiecare secundă.
# Procesul "Receiver" primește mesajele și le scrie într-un fișier.
# Oprește procesul după ce au fost trimise 10 mesaje.

import multiprocessing
from time import sleep

def producer(channel):
    for i in range(10):
        channel.send(f"This is message {i}")
        sleep(1)
    channel.send("DONE")  # Semnalizează sfârșitul producției

def consumer(channel):
    while True:
        msg = channel.recv()
        if msg == "DONE":  # Termină când primește mesajul special
            print("Consumer: Finished receiving messages.")
            break
        print(msg)

if __name__ == '__main__':
    parent, child = multiprocessing.Pipe()

    pp = multiprocessing.Process(target=producer, args=(parent,))
    cp = multiprocessing.Process(target=consumer, args=(child,))

    pp.start()
    cp.start()

    pp.join()
    cp.join()
