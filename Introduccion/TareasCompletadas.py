import logging
import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)


URLS = [
    'https://twitter.com/home',
    'https://www.youtube.com',
    'https://www.google.com',
    'https://gitlab.com',
    'https://stackoverflow.com',
    'https://github.com'
]
def generate_request(url):
    return requests.get(url), url #Cuando retornas más de 1 objeto se vuelve una tupla

def check_status(response, url):

    logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def math_opetation(num1,num2):
    return num1+num2

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='SuperHiloDeEduardoCool') as executor:
        futuros  = [executor.submit(generate_request, url) for url in URLS ]

                                            #Al utilizar as_completed nos evitamos usar 
        for futuro in as_completed(futuros):#La función as_completed recibe como argumentos una lista de futuros
                                            #Iteramos la lista para realizar los correspondientes métodos
            response, url = futuro.result() #GenerateRequest genera una dupla, y así lo asignamos

            if response.status_code == 200: 

                check_status(response, url)


        future = executor.submit(math_opetation, 10,10)
        future.add_done_callback(
            lambda future: logging.info(f'El resultado de la operación es {future.result()}')
        )