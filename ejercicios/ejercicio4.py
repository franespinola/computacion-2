import argparse
from tabnanny import verbose
import time
import os




def main():

    parser = argparse.ArgumentParser(description='.')

    parser.add_argument("-n", "--numero1", type=int, help="numero de procesos")
    parser.add_argument("-r", "--recursive", type=int, help="repeticiones")
    parser.add_argument("-f", "--path", type=str, help="path")
    parser.add_argument("-v", "--verbose", help="modo de texto visible",action="store_true")
    args = parser.parse_args()

    file = open(args.path, "w")            ##with open(args.path,'w+') as file:
    numero1=args.numero1                        #for i in range(numero1):
    rec=args.recursive
    verbose=args.verbose
    
    abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range (numero1):
        if os.fork()==0:
            for r in range(rec):
                if verbose:
                    print(f'Proceso {os.getpid()} escribiendo letra: {abc[i]}')
                file.write(f'{abc[i]}')
                file.flush()
                time.sleep(1)
            os._exit(0)
    os.wait()
    file.close()
    

    text=open(args.path, "r")
    for letter in text.readlines():     #readlines()devuelve cada linea escrita en el archivo como una lista
        print(letter)
    text.close()

if __name__ == "__main__":
    main()



        