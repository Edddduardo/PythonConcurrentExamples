import threading
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def callback():
    logging.info('Hola, soy el callback programado')

if __name__ == '__main__':
    thread = threading.Timer(3,callback)
    thread.start()


    logging.info('Soy el hilo principal y estoy esperando al otro')