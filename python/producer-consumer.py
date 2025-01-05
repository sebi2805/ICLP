import logging
import threading
import time

# Configurarea logging-ului pentru afișarea mesajelor
logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

# Variabile globale
items = []
condition = threading.Condition()

# Clasa Consumer
class Consumer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def consume(self):
        with condition:
            while len(items) == 0:  # Folosim while în loc de if pentru a evita "spurious wakeups"
                logging.info('No items to consume, waiting...')
                condition.wait()
            items.pop()
            logging.info('Consumed 1 item')
            condition.notify_all()  # Notificăm toți ceilalți thread-uri

    def run(self):
        for _ in range(10):  # Consumă 10 elemente
            time.sleep(2)  # Simulează consumul unui element
            self.consume()

# Clasa Producer
class Producer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def produce(self):
        with condition:
            while len(items) >= 10:  # Limitează lista la 10 elemente
                logging.info('Too many items, waiting...')
                condition.wait()
            items.append(1)
            logging.info('Produced 1 item')
            condition.notify_all()  # Notificăm toți ceilalți thread-uri

    def run(self):
        for _ in range(10):  # Produce 10 elemente
            time.sleep(1)  # Simulează producerea unui element
            self.produce()

# Funcția principală
def main():
    producers = [Producer(name=f'Producer-{i}') for i in range(3)]  # 3 producători
    consumers = [Consumer(name=f'Consumer-{i}') for i in range(2)]  # 2 consumatori

    # Pornim toți producătorii și consumatorii
    for producer in producers:
        producer.start()
    for consumer in consumers:
        consumer.start()

    # Așteptăm să se termine toți producătorii și consumatorii
    for producer in producers:
        producer.join()
    for consumer in consumers:
        consumer.join()

if __name__ == "__main__":
    main()
