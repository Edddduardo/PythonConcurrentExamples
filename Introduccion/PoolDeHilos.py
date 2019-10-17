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
    executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix='EduardoHiloCool')  #Colocamos el máximo de hilos que pueda utilizar
    #La picina nos permite generar la N cantidad de hilos que sean necesarios
    #Se reciclan los hilos para evitar consumo de procesador 




    #Reutilización de Threads. 
    #Si todos los hilos se encuentran ocupado se añaden a la cola
    executor.submit(math_opetation,10,20)
    executor.submit(math_opetation,20,20)
    executor.submit(math_opetation,50,50)
    executor.submit(math_opetation,100,200)