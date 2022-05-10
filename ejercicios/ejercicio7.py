''''
Escribir un programa que genere dos hijos utilizando multiprocessing.

Uno de los hijos deberá leer desde stdin texto introducido por el usuario, y deberá escribirlo en un pipe (multiprocessing).

El segundo hijo deberá leer desde el pipe el contenido de texto, lo encriptará utilizando el algoritmo ROT13, y lo almacenará en una cola de mensajes (multiprocessing).

El primer hijo deberá leer desde dicha cola de mensajes y mostrar el contenido cifrado por pantalla.
'''
import multiprocessing
import sys
import codecs

def main():
    r,w = multiprocessing.Pipe()
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=escritor,args=(r,q))
    p2 = multiprocessing.Process(target=lector,args=(w,q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
def escritor(w,q):
    recv=w.recv()       #traigo lo q escribi por el otro lado
    encriptacion = codecs.encode(recv, 'rot_13')
    q.put(encriptacion)
    w.close()
def lector(r,q):
    sys.stdin = open(0)
    std = sys.stdin.readline()
    r.send(std)
    r.close()
    print(f"texto encriptado:{q.get()}")


if __name__ == "__main__":
    main()
    

 