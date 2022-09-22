import requests
import threading

def get_services(dato=0):
    print(f'Dato={dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)

if __name__ == '__main__':
    for x in range(0,50):
        th1 = threading.Thread(target=get_services, args=[x])
        th1.start()
        #get_services()

