# 3. Multiprocessing: Manager de Procese
# Creează un program care:

# Utilizează multiprocessing.Manager pentru a partaja o listă între procese.
# Creează două procese: unul care adaugă valori aleatorii în listă și unul care calculează suma elementelor din listă la fiecare 2 secunde.
# Oprește execuția proceselor după 10 secunde.
import multiprocessing
import random
import time

def add_values(shared_list):
    """Adaugă valori aleatorii în lista partajată."""
    while True:
        value = random.randint(1, 100)
        shared_list.append(value)
        print(f"Procesul de adăugare a adăugat: {value}. Lista: {list(shared_list)}")
        time.sleep(1)  # Pauză pentru a simula adăugarea treptată

def calculate_sum(shared_list):
    """Calculează și afișează suma elementelor din lista partajată."""
    while True:
        total = sum(shared_list)
        print(f"Procesul de calculare a sumei: Suma curentă este {total}. Lista: {list(shared_list)}")
        time.sleep(2)  # Pauză de 2 secunde între calcule

if __name__ == "__main__":
    # Manager pentru lista partajată

    with multiprocessing.Manager() as manager:
        shared_list = manager.list()  # Creează lista partajată
        
        # Crearea proceselor
        process_adder = multiprocessing.Process(target=add_values, args=(shared_list,))
        process_summer = multiprocessing.Process(target=calculate_sum, args=(shared_list,))
        
        # Pornirea proceselor
        process_adder.start()
        process_summer.start()
        
        # Rulează procesele timp de 10 secunde
        time.sleep(10)
        
        # Termină procesele
        process_adder.terminate()
        process_summer.terminate()
        
        # Așteaptă închiderea proceselor
        process_adder.join()
        process_summer.join()
        
        print("Execuția proceselor s-a încheiat.")




# mie imi place mai mult cu pipe
import multiprocessing
import random
import time

def producer(pipe_conn):
    """Trimite valori aleatorii prin pipe."""
    while True:
        value = random.randint(1, 100)
        pipe_conn.send(value)  # Trimite valoarea prin pipe
        print(f"Producătorul a trimis: {value}")
        time.sleep(1)  # Pauză pentru a simula generarea valorilor

def consumer(pipe_conn):
    """Primește valori prin pipe și calculează suma."""
    current_sum = 0
    while True:
        if pipe_conn.poll():  # Verifică dacă sunt date disponibile în pipe
            value = pipe_conn.recv()  # Primește valoarea
            current_sum += value
            print(f"Consumatorul a primit: {value}, Suma curentă: {current_sum}")
        time.sleep(2)  # Pauză între afișări

if __name__ == "__main__":
    # Crearea pipe-ului
    parent_conn, child_conn = multiprocessing.Pipe()

    # Crearea proceselor
    producer_process = multiprocessing.Process(target=producer, args=(parent_conn,))
    consumer_process = multiprocessing.Process(target=consumer, args=(child_conn,))

    # Pornirea proceselor
    producer_process.start()
    consumer_process.start()

    # Rulează procesele timp de 10 secunde
    time.sleep(10)

    # Termină procesele
    producer_process.terminate()
    consumer_process.terminate()

    # Așteaptă închiderea proceselor
    producer_process.join()
    consumer_process.join()

    print("Execuția proceselor s-a încheiat.")
