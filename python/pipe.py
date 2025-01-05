import random
from time import sleep
from multiprocessing import Process, Pipe

# Funcția procesului sender
def sender(connection):
    print('Sender: Running', flush=True)
    for i in range(10):
        value = random.random()  # Generează o valoare aleatoare
        sleep(value)             # Simulează o întârziere
        connection.send(value)   # Trimite valoarea prin conexiune
    connection.send(None)        # Trimite semnalul de finalizare
    print('Sender: Done')

# Funcția procesului receiver
def receiver(connection):
    print('Receiver: Running', flush=True)
    while True:
        value = connection.recv()  # Primește valoarea
        if value is None:          # Dacă valoarea este None, se oprește
            break
        print(f'Receiver: Got value {value}')
    print('Receiver: Done')

# Punctul principal al programului
if __name__ == '__main__':
    conn1, conn2 = Pipe()  # Creează o structură Pipe

    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()

    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
