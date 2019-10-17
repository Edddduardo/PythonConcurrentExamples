import os
import logging
import time 
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s -> %(processName)s: %(message)s'
)
def nuevo_proceso():
    logging.info('Hola soy un nuevo proceso')
    time.sleep(3)
    logging.info('Hola soy el final del proceso')

if __name__ == '__main__':
    process =multiprocessing.Process(target=nuevo_proceso, name='CosoHijo')
    process.start()

    logging.info('Hola soy el proceso padre')