from threading import Semaphore, Thread
import pytube

"""
wait(s) - decrementa el valor de s si este es mayor que cero. Si es igual a cero, el proceso se bloqueara en el semaforo hasta que otro proceso llame a signal().
signal(s) - desbloquea algun proceso bloqueado en s, y en el caso de que no haya ningun proceso bloqueado, incrementa el valor de s.

"""

semaphore = Semaphore(1)

    
def crito(url,path):
    print(f"Descargando video: {url}")
    try:
        pytube.YouTube(url).streams.first().download(path)
        titleyt = pytube.YouTube(url).title
        print(f"Video descargado: {titleyt}\nURL: {url}\n")
    except Exception as err:
        print('Error en la descarga: ', err) 


class Hilo(Thread):
    def __init__(self, url, path):
        Thread.__init__(self)
        self.url = url
        self.path=path
    def run(self):
        semaphore.acquire()
        crito(self.url, self.path)
        semaphore.release()
link = ["https://www.youtube.com/watch?v=9pqC4ivoi7c",
            "https://www.youtube.com/watch?v=C4h75g7A9Wo",
            "https://www.youtube.com/watch?v=K1gHajTNDTE",
            "https://www.youtube.com/watch?v=MTn9lGKBteA",
            "https://www.youtube.com/watch?v=CIDKz3TGJhY"]
path = "/home/enrique/Vídeos"        
threads_semaphores = [Hilo(link[0],path), Hilo(link[1],path), Hilo(link[2],path), Hilo(link[3],path), Hilo(link[4],path)]

for t in threads_semaphores:
    t.start()