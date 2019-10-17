import logging
import multiprocessing
import time 
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

def proceso_hijo():
    logging.info('Soy un proceso hijo')

    time.sleep(30)
    logging.info('Fin del proceso hijo')




if __name__ == '__main__':
    proceso = multiprocessing.Process(target=proceso_hijo)
    proceso.start()
    time.sleep(2)
    if proceso.is_alive(): #Retorna un booleano diciendo si está vivo o no 
        proceso.terminate() #Terminar un proceso antes de tiempo
        logging.info('Proceso hijo terminado antes de tiempo')
    logging.info('Fin del programa')