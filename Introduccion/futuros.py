import logging
import threading
import time
from concurrent.futures import Future


logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def callback_futuro(future): #Los callbacks de future siempre deben de recibir como parametro un result
    logging.info('Soy un callback que espera que futuro tenga un valor')
    logging.info(f'El futuro es {future.result()}')


if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_futuro) #Para que se ejecute la función de parametro cuando tenga un valor
    future.add_done_callback(
        lambda future: logging.info('Hola soy un lambda!')
    )
    logging.info('Comienza tarea compleja')
    time.sleep(2)
    logging.info('Terminando tarea compleja')
    logging.info('Asignando valor a Futuro')
    future.set_result('Eduardo es cool') #Asignamos valor a future 
    logging.info('Futuro ya tiene un valor')
