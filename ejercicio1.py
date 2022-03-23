#Ejercicio 1 - Getopt

"""Crear una calculadora, donde se pase como argumentos luego de la opción -o el operador que se va a ejecutar (+,-,*,/), luego de -n el primer número de la operación, y de -m el segundo número.

Ejemplo:

python3 calc.py -o + -n 5 -m 6

5 + 6 = 11

Considerar que el usuario puede ingresar los argumentos en cualquier orden. El programa deberá verificar que los argumentos sean válidos (no repetidos, números enteros, y operaciones válidas."""


import getopt
import sys


argv=sys.argv[1:]
opt,arg=getopt.getopt(argv,'o:m:n:')                   #argv=lista de argumento a analizar, la ponemos en 1 ya que en la posicion 0 es el nombre de nuestro archivo

print(opt)



for op,arg in opt:
    if op=='-o':
        if arg not in "*/+-":
            print("operador no valido")
            exit()
        operador = arg
    elif op=='-m':
        try:
            num1=int(arg)
        except ValueError:
            print("numero invalido")
            exit()
    elif op=='-n':
        try:
            num2=int(arg)
        except ValueError:
            print("numero invalido")
            exit()
