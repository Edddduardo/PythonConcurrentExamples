import threading

def ejecutar_a(id):
    for x in range(0,10): 
        print(f'Soy el hilo {id} en la vuelta {x}') #f en cada print porque lleva variables. 
def ejecutar_b(id):
    for x in range(0,10):
        print(f'Soy el hilo {id} en la vuelta {x}')
def ejecutar_c(id):
    for x in range(0,10):
        print(f'Soy el hilo {id} en la vuelta {x}')

thread_a = threading.Thread(target=ejecutar_a, args=[1]) #Se puede enviar como lista
thread_b = threading.Thread(target=ejecutar_b, args=(2,)) #Se puede enviar como tupla, SIEMPRE se finaliza con una ","
thread_c = threading.Thread(target=ejecutar_c, kwargs={'id': 3}) #Se puede enviar como diccionario

thread_a.start()
thread_b.start()
thread_c.start()
