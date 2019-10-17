import logging
import threading
import time
import requests
#from concurrent.futures import map
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)
 #La función map() ejecura una lista

URLS = [
    'https://twitter.com/home',
    'https://www.youtube.com',
    'https://www.google.com',
    'https://gitlab.com',
    'https://stackoverflow.com',
    'https://github.com'
]
def generate_request(url):
    return requests.get(url)

def check_status(response, url):

    logging.info(f'La respuesta del servidor {url} es: {response.status_code}')

def math_opetation(num1,num2):
    return num1+num2

if __name__ == '__main__':  
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='SuperHiloDeEduardoCool') as executor:                                                           
        result = executor.map(generate_request,URLS) #Recibe una función y un lista iterable       
        for url, response in zip(URLS,result): 
                       
            if response.status_code == 200: 
                check_status(response, url)

        future = executor.submit(math_opetation, 10,10)
        future.add_done_callback(
            lambda future: logging.info(f'El resultado de la operación es {future.result()}')
        )