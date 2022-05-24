import multiprocessing
import argparse
import numpy as np

#pull=multiprocessing.Pool() # si no especifico me da la cantidad de nucleos q tengo en mi caso 4
#print(pull)

#cuando creo los procesos hijos aparecen suspendidos en S+ si es q no tienen asignadas tareas
#podemos tirar las funciones de distinta forma: ver final clase
#   map.apply
#   imap manda los resultados desordenados
#   map lo manda ordenado

'''
Realizar un programa en python que reciba por argumentos:

    -p cantidad_procesos

    -f /ruta/al/archivo_matriz.txt
    -c funcion_calculo

El programa deberá leer una matriz almacenada en el archivo de texto pasado por argumento -f, y deberá calcular la funcion_calculo para cada uno de sus elementos.

Para aumentar la performance, el programa utilizará un Pool de procesos, y cada proceso del pool realizará los cálculos sobre una de las filas de la matriz.

La funcion_calculo podrá ser una de las siguientes:

    raiz: calcula la raíz cuadrada del elemento.
    pot: calcula la potencia del elemento elevado a si mismo.
    log: calcula el logaritmo decimal de cada elemento.
'''


def main():
    parser = argparse.ArgumentParser(description='Ingresar nombre de los archivos.')

    parser.add_argument("-p", "--process", type=str, help="proceso")
    parser.add_argument("-f", "--route", type=str, help="ruta")
    parser.add_argument("-c", "--function", type=str, help="function")  #podra ser raiz(raiz cuadrada del elemento),pot(potencia del elemento elevado a si mismo),log(calcula logaritmo decima de cada elemento)
    
    procesos=parser.parse_args().process
    funcion=parser.parse_args().function

    matriz=

    pool=multiprocessing.Pool(processes=procesos)

    pool.starmap(funcion,)

    

def cuadrado(a):
    return a*a
def potencia(a):
    return a^a
def logaritmo(a):
    return np.log(a)
    

if __name__=="__main__":
    main()