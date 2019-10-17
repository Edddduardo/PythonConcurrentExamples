import logging
import threading
import time
import requests

logging.basicConfig(
    level=logging.DEBUG,
    format='%(threadName)s:%(message)s'
)

user = dict()


def gerate_request(url, event):
    global user 
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()

        user = response_json.get('results')[0]
        event.set()

def show_username(event):
    event.wait()
    name = user.get('name').get('first')
    logging.info(f'El nombre del usuario es {name}')

if __name__ == '__main__':
    event = threading.Event()
    thread1 = threading.Thread(target=gerate_request, args=('https://randomuser.me/api', event,))
    thread2 = threading.Thread(target=show_username, args=(event,))

    thread1.start()
    thread2.start()