import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)

class ThreadEduardo(threading.Thread):
    def __init__(self, name,daemon):
        threading.Thread.__init__(self, name=name, daemon=daemon)

    def run(self):
        while True:
            logging.info('Aqui se ponen tareas concurrentes')
            time.sleep(1)



if __name__ == '__main__':
    thread = ThreadEduardo('RastaEduardo',True)
    thread.start()

    time.sleep(3)
    logging.info('Taran')