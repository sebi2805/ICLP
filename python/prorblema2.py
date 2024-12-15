import os
import threading


class Consumer():
    def __init__(self, path):
        self.path = path

        result = threading.Thread(target=self.consume)
        result.start()
        try:
            result.join()
        except:
            print("It did throw an error ")
            pass

        print("The result is: ", result)
    
    def consume(self):
        with open(self.path, 'r') as file:
            return file.read()
        # deserializare

class Producer():
    def __init__(self, path):
        self.path = path
        self.consumers = [Consumer(self.path) for _ in range(4)]

    def produce(self):
        