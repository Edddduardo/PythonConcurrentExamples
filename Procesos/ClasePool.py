import logging
from multiprocessing import Pool

logging.basicConfig(
    level=logging.DEBUG,
    format='%(processName)s: %(message)s'
)

def is_even(num):
    return num % 2 ==0


if __name__ == '__main__':
    with Pool(processes=2) as executor: #Retorna lo que la función retorna, no cómo el submit
        result = executor.apply(is_even,args=(10,))

        logging.info(f'El resultado es {result}')