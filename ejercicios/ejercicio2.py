import argparse
from asyncore import write
from io import open
import os
def main():
    parser = argparse.ArgumentParser(description='Ingresar nombre de los archivos.')

    parser.add_argument("-f", "--file1", type=str, help="archivo 1")
    parser.add_argument("-s", "--file2", type=str, help="archivo 2")
    args = parser.parse_args()

    print(args.file1, args.file2) #muestro los argumentos

    file1=args.file1
    file2=args.file2


    if os.path.isfile(file1):
        with open(file1,'r') as file:
            f=file.read()
        with open(file2,'w+') as output:
            output.write(f)
        file.close()
        output.close()
        
    else:
        print("el archivo no existe")

'''
archivo_texto= open(file1,"w")
archivo_texto.write(file2)
archivo_texto.close()
'''

''''
try:
    file=open(args.file1)
    print(file)
    file.close()
except FileNotFoundError:
    print('el archivo no existe')
    exit()
'''

main()


