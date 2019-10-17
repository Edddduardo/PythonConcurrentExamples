import logging
import threading
import requests
from concurrent.futures import Future

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')
        logging.info(f'El nombre del pokemon es {name}')
    

def generate_request(url):
    future = Future() #Los futures son como las promesas en JS, tendrán un valor más adelante
    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url)) #Enviamos el resultado de la operación en el hilo y le damos un 
                                                    #valor a future.
    ))
    thread.start()

    return future #Retorna el future pero con un valor 

if __name__ == '__main__':
    future = generate_request('https://pokeapi.co/api/v2/pokemon/1/')
    future.add_done_callback( #Esto espera a que tenga un valor para ejecutar alguna función
        lambda future: show_pokemon_name(future.result()) #Esto retorna el valor que tiene future a la función, porque aqui ya tiene un valor
    )

    while not future.done(): #Aqui vamos a imprimir hasta que future tenga un valor 
        logging.info('A la espera de un resultado')
    else:
        logging.info('Terminamos el programa')