import logging
import threading
import time
import requests
from concurrent.futures import ThreadPoolExecutor

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

def check_status(response):

    logging.info(f'La respuesta del servidor {response[1]} es: {response[0].status_code}')

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='SuperHiloDeEduardoCool') as executor:
        futuros  = [executor.submit(generate_request, url) for url in URLS ]

        for futuro in futuros: 
            futuro.add_done_callback(
                lambda future: check_status(future.result())
            )