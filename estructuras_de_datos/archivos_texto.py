##con la funcion open abrimos un archivo de texto donde como parametro el nombre del archivo y la letra w escritoria r para leer, a para agregar/escrbir y x para buscar en espcial, si no exista da erro
### con write escrimibimos el cambio


import random 
f = open('numeros.txt','w') ### se abre un archivo para escribir con w, si no existe se crea

for count in range(100):  ##count para recorrer 100 elementos
    num = random.randint(1,1000) ##num se asignar a random con la funcion entre 1 a 1000
    f.write(str(num)+'\n') #se escribe el resultado en la impresion del archivo de texto
f.close() ##se cierra la funcion y se escribe todo


