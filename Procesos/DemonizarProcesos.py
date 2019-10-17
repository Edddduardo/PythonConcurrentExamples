import os
import logging
import time 
import multiprocessing

logging.basicConfig(
    level=logging.DEBUG,
    format='%(process)s -> %(processName)s: %(message)s'
)
def nuevo_proceso(nuevoMensaje):
    logging.info('Hola soy un nuevo proceso')
    time.sleep(3)
    logging.info(nuevoMensaje)
    logging.info('Hola soy el final del proceso')

if __name__ == '__main__':
    process =multiprocessing.Process(target=nuevo_proceso, name='CosoHijo',
                kwargs={'nuevoMensaje':'Soy el mensaje mas cool!!!!'},
                daemon=True)
    
    
    process.start()

    logging.info('Hola soy el proceso padre')