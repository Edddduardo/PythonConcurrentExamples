import time
import logging
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)
def nueva_tarea():
    current_thread = threading.current_thread()
    name = current_thread.getName()
    id = threading.get_ident()

    logging.info(f'El thread principal es: {current_thread} y su nombre es {name}')
    logging.info(f'El ID actual es {id}')



if __name__ == '__main__':
    thread = threading.Thread(target=nueva_tarea, name='RastaDeEduardo')
    thread.start()

    logging.info(f'Los thread vivos son {threading.enumerate()}')


    for threads in threading.enumerate():
        if threads == threading.main_thread():
            logging.info('Thread principal')
        logging.info(threads)