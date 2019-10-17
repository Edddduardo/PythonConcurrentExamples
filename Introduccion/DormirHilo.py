import time
import logging
import threading


#sleep(segundos) EEJJJJJ: 0.5


logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s : %(message)s'
)

def task():
    logging.info('Se ejecuta una nueva tarea')
    time.sleep(2)
    logging.info('Se terminó la nueva tarea')


if __name__ == '__main__':
    #thread = threading.Thread(target=task)
    #thread.start()

    contador=0

    while True:
        time.sleep(1)
        contador+=1
        logging.info(f'Tiempo transcurrido: {contador} segundos')

