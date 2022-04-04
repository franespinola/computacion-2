import os

def main():
   
    retorno = os.fork()
    print("---------------------------------------------------------")
    if retorno == 0:
        print("hola mundo,soy el hijo")
    else:
        print(f"hola mundo,retorno:{retorno}")

main()