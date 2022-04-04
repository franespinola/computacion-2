import argparse
import os
import time

def main():
    
    parser = argparse.ArgumentParser(description='.')

    parser.add_argument("-n", "--numero1", type=int, help="numero de procesos")
    parser.add_argument("-v", "--verbose", help="modo de texto visible",action="store_true")
    args = parser.parse_args()

    numero1=args.numero1
    verbose=args.verbose
  
  ## cada hijo calculara la suma de los numeros pares que van de 0 hasta su numero de PID
  ## el verbose mostrara un mensaje al inicio y al final de la ejecución de cada proceso hijo, que indique su inicio y fin.
	
   
    def sumapares():          
        sum=0
        for i in range(os.getpid()):
            if i%2==0:
                sum+=i
        print(f'{os.getpid()}-{os.getppid()}:{sum}')    

    for i in range(numero1):
        procesos=os.fork()
        if procesos==0:
            if verbose:
                print("iniciando proceso")    
            sumapares()
            if verbose:
                print("finalizando proceso")
            os._exit(0)
    os.wait()


if __name__=="__main__":
    main()
