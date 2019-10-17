import logging

# Existen diferentes tipos de mensajes con Logggin
# Debug (10), Info (20), Warning (30), Error (40), Critical (50)

#Si ejecuto así, el programa sólo muestra las superiores a nivel 30

#Para mostrar las superiores a nivel 30 se utiliza lo siguiente 

logging.basicConfig( #Esto es para colocar a partir de qué nivel queremos que se muestre, de lo contrario de 30 para arriba
    level=10,

    #Para personalizar el mensaje en la consola se hace lo siguiente: 
    format='%(message)s ----- fecha : %(processName)s',
    #filename es para que imprima el nombre del archivo que ejecuta la sentencia. 
    #asctime es para obtener el tiempo en el que se está realizando la sentencia. 
    #message para obtener el mensaje del logg
    #funcName es para obtener el nombre de la función que ejecuta
    #levelname para obtener el tipo de mensaje que se realizó
    #lineno obtiene el número de la línea que se está ejecutando
    #name obtiene nombre del logg
    #pathname obtiene la ruta 
    #LAS QUE IMPORTAN AHORA
    #thread obtiene el hilo que se está ejecutando
    #threadName obtiene el nombre del hilo que se está ejecutando
    #process obtiene el proceso que se está ejecutando
    #processName obtiene el nombre del proceso que se está ejecutando



    #Para agregar formato a la fecha que estamos agregando, se hace lo siguiente:
    #datefmt='%H:%M:%S', #Para sólo obtener hora, minuto y segundo

    filename='mensajes.txt' #Esto es para colocar el nombre del archivo y que coloque los logg ahí
)

def mensajazos():
    logging.debug('Este es un mensaje tipo Debug')
    logging.info('Este es un mensaje tipo Info')
    logging.warning('Este es un mensaje tipo Warning')
    logging.error('Este es un mensaje tipo Error')
    logging.critical('Este es un mensaje tipo Critical')

if __name__ == '__main__':
    mensajazos()