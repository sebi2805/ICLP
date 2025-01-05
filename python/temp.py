import logging
import threading
logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')
def thread_function():
    print(f'Thread  started')

if __name__ == '__main__':
    t1 = threading.Thread(target=thread_function)
    t2 = threading.Thread(target=thread_function)

    t1.start()
    t2.start()