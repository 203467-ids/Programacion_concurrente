import requests
import psycopg2
import concurrent.futures
import threading
import pytube

def service1(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
    print("hilo1 terminado")
        
def service2(urls,path):
    
    for url in urls:
        hilov = threading.Thread(target=get_service2, args=[url,path])
        hilov.start()
    
    print("hilo2 terminado")
def service3(dato=0):
    print(f'Dato={dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print("hilo3 terminado")

def get_service(url):
    response = requests.get(url)
    if response.status_code == 200 :
        data = response.json()
        for dataout in data:
           
             write_db(dataout["title"])
            
    else:
        print(response.status_code)

def get_service2(url,path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        titleyt = pytube.YouTube(url).title
        print(f"Video descargado: {titleyt}\nURL: {url}\n")
    except Exception as err:
        print('Error en la descarga: ', err) 

def connect_db():
    try:
        credenciales = {
        "dbname": "postgres",
        "user": "tester",
        "password": "tester2022",
        "host": "localhost",
        "port": 5432
        }
        conexion=psycopg2.connect(**credenciales)
        
        return conexion
    except psycopg2.Error as e:
          print("Ocurrió un error al conectar a PostgreSQL: ", e)

def write_db(dato):
    sql = """INSERT INTO dato(name) VALUES(%s);"""

    try: 
        
        cur = conn.cursor()
        cur.execute(sql, (dato,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pass

if __name__ == "__main__":
    conn=connect_db()
    link = ["https://www.youtube.com/watch?v=9pqC4ivoi7c",
            "https://www.youtube.com/watch?v=C4h75g7A9Wo",
            "https://www.youtube.com/watch?v=K1gHajTNDTE",
            "https://www.youtube.com/watch?v=MTn9lGKBteA",
            "https://www.youtube.com/watch?v=CIDKz3TGJhY"]
   
    url= ["https://jsonplaceholder.typicode.com/posts"]
    path = "/home/enrique/Vídeos"
    for x in range(0, 50):
        th1 = threading.Thread(target=service1, args=[url])
        th1.start()
    
    th2 = threading.Thread(target=service2, args=[link, path])
    th2.start()

    for x in range(0,50):
        th3 = threading.Thread(target=service3, args=[x])
        th3.start()

