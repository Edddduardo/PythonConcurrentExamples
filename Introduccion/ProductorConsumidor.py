import logging
import time
import queue
import threading
import random

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)
queue = queue.Queue(maxsize=10) #Determinamos el tamaño

def productor():
    while True:
        if not queue.full():
            item = random.randint(1,10)
            queue.put(item)
            logging.info(f'Este es el numero elemento en la cola {item}')
            time_to_sleep = random.randint(1,3)
            time.sleep(time_to_sleep)

def consumidor():
    while True: 
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            logging.info(f'Nuevo elemento obtenido {item}')
            time_to_sleep = random.randint(1,3)
            time.sleep(time_to_sleep)




if __name__ == '__main__':
    productor2 = threading.Thread(target=productor)
    consumidor2 = threading.Thread(target=consumidor)

    productor2.start()
    consumidor2.start()

