# uso barrier para usar mas facilmente semaforo,coloco el valor de acuerdo a la cantidad de hilos q tenga. Es como poner un punto de encuentro coloco tantas barreras como funciones tenga, estas van adentro de cada una

#acquire seria como un wait
#release seria como un signal para despertar al proceso dormido 

# with es como hacer un wait y un signal todo junto


'''
Sincronizacion event/condition [event] (opcional) Tarea

Escribir un programa que reciba por argumento la opción -f acompañada de un path_file.
Etapa 1:

El programa deberá crear una memoria compartida (variable global, queue, etc.), y generar dos hilos: H1 y H2

El hilo H1 leerá desde el stdin línea por línea lo que ingrese el usuario.

Cada vez que el usuario ingrese una línea, H1 la almacenará en la memoria compartida, y notificará, mediante event/condition, al hilo H2.

El hilo H2 al recibir la notificación leerá la línea desde la memoria compartida la línea, y la almacenará en mayúsculas en el archivo pasado por argumento (path_file).
'''