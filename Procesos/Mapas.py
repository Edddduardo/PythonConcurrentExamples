import logging
import time
from multiprocessing import Pool

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

def is_even(num):
    time.sleep(1)
    return num % 2 ==0

def show_result(results):
    logging.info(f'El resultado es {results}')



if __name__ == '__main__':
    with Pool(processes=2) as executor:
        numbers = [number for number in range(1,15)]       
        #map_result=executor.map_async(is_even,numbers, callback=show_result) #Proceso del map, que recibe una función y un objeto iterable pero asincrono       
        for element in executor.imap_unordered(is_even,numbers) : #El imap_unordered retorna un objeto iterable
            logging.info(element)
        # logging.info('Esperamos a que los resultados estén listos')
        # map_result.wait()
        