import logging
import time
from multiprocessing import Pool

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

def is_even(num):
    time.sleep(3)
    return num % 2 ==0


if __name__ == '__main__':
    with Pool(processes=2) as executor: #Retorna lo que la función retorna, no cómo el submit
        apply_result = executor.apply_async(is_even,args=(10,))


        logging.info('Espera hasta que apply_result tenga un valor ')
        apply_result.wait(timeout=3) #Espera hasta que posea un valor y timeout es lo maxmimo que espera
        logging.info(f'El resultado es {apply_result.get(timeout=2)}') 

        # result = executor.apply(is_even,args=(20,))
        # logging.info(f'El resultado es {result}')

        logging.info('Fin del programa')