import os,sys,argparse


def main():
    
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument("-f", "--file", type=str, help="numero de procesos")
    args = parser.parse_args()
    archivo= args.file

    with open(archivo,'w') as w:
        w.write("hola mundo\ncomo estas\ntodo bien\n")
    archivo_open=open(archivo,"r")
    archivo_lista=archivo_open.readlines()
    archivo_open.close()

    #print(archivo_lista)
        
    for i in range(len(archivo_lista)):
        r,w=os.pipe()
        processid=os.fork()
        if processid:
            os.close(r)
            w=os.fdopen(w,'w')
            w.write(archivo_lista[i])
            w.close()
            os.wait()
            sys.exit(0)
        else:
            os.close(w)
            r=os.fdopen(r,'r')
            child_line=r.readline()
            print(f"{child_line[::-1].strip()}")
            r.close()

main()

   



