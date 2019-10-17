import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s'
)

def conexion_DB(): #Simula una acción que tome tiempo en procesar
    logging.info('Hace una petición al DB y cosas así de DB')
    time.sleep(2.5)

def conexion_WS(): #Simula una acción que tome tiempo en procesar
    logging.info('Hace una petición al WS y cosas así de WS')
    time.sleep(2)

if  __name__ == '__main__':
    thread1= threading.Thread(target=conexion_DB)
    thread2= threading.Thread(target=conexion_WS)

    thread1.start()
    thread2.start()

    
    thread1.join() #Duermen los hilos principales en espera de que terminen
    thread2.join() #Normalmentese usa cuando se encuentra a la espera de un resultado para continuar las ejecuciones

    logging.info('Los hilos terminaron')

