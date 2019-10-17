import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)


def math_opetation(num1, num2): 
    time.sleep(1)
    result = num1 + num2
    logging.info(f'El resultado de {num1} + {num2} = {result}')



if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix='SuperHiloDeEduardoCool') as executor:
        executor.submit(math_opetation,10,20)
        executor.submit(math_opetation,20,20)
        executor.submit(math_opetation,50,50)
        executor.submit(math_opetation,100,200)

        executor.shutdown() #Apaga el executor para no permitir otra tarea