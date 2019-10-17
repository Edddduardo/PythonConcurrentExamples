import time
import queue
import threading
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)

def show_elements():
    while not queue.empty():
        item = queue.get()

        logging.info(f'El elemeto de la cola es : {item}')

        queue.task_done()

        time.sleep(0.5)


if __name__ == '__main__':
    queue = queue.Queue() #FIFO

    for val in range(1,20):
        queue.put(val)

    logging.info('La cola ya tiene datos')

    for _ in range(4):
        thread = threading.Thread(target=show_elements)
        thread.start()