#Ejercicio 1 - Getopt


import getopt
import sys


#opt=operador
#arg=argumento

def main():
    argv=sys.argv[1:]
    try:   
        opts,args=getopt.getopt(argv,'o:m:n:')                   #argv=lista de argumento a analizar, la ponemos en 1 ya que en la posicion 0 es el nombre de nuestro archivo
    except getopt.GetoptError as err:
        print(err)
        sys.exit()
    for opt, arg in opts: 
        if opt == '-o':            
            if arg in '+-*/':
                operador=arg
            else:
                print("operacion incorrecta")
                exit()
        elif opt == '-m':
            try:
                numM=int(arg)
            except ValueError:
                print("numero invalido")
                exit() 
        elif opt == '-n':
            try:
                numN=int(arg)
            except ValueError:
                print("numero invalido")
                exit()
    if operador == '+':
        return print(numM+numN)
    elif operador == '-':
        return print(numM-numN)
    elif operador == '*':
        return print(numM*numN)
    else:
        return print(numM/numN)


main()
   
          



    

   

  
        

        
   
