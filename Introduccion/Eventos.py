import logging 
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)

def Thread1(event):
    logging.info('Espero la señal de arranque')
    event.wait() #Espera hasta que la señal sea dada
    logging.info('La señal fue dada, la bandera es True')

def Thread2(event):
    
    while not event.is_set(): #Pregunta si la señal está dada
        logging.info('Esperando señal')
        time.sleep(0.5)
    




if __name__ == '__main__':
    event = threading.Event() #Los eventos tienen banderas, al inicializarlos están en false 
    thread1 = threading.Thread(target=Thread1, args=(event,))
    thread2 = threading.Thread(target=Thread2, args=(event, ))

    thread1.start()
    thread2.start()
    time.sleep(3)

    event.set() #Cambiamos la bandera a True para que otra cosa se ejecute 

    #event.clear() #Con esto regresamos la bandera a False