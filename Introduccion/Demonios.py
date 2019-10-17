import logging
import threading
import requests
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def thread():
    logging.info('Hola, soy un hilo normalito')
    time.sleep(2)
    logging.info('El programa muere cuando yo muero')


def daemon_thread():
    while True:
        logging.info('Esto es un hilo demonio, estoy en background')
        time.sleep(0.5)


if __name__ == '__main__':
    thread = threading.Thread(target=daemon_thread, daemon=True)
    thread.start()
    input('Presiona algo para que se muera')