import numpy as np 

arreglo = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
##imprimimos los arreglos

print(arreglo)
reshapeArreglo = arreglo.reshape(3,5);
###creamos una forma nueva, teniendo unos arreglo der 15,  y lo dividimos en 3 de 5, dandomo como resultado 3 arreglos de 5

print(reshapeArreglo);

arregloReshape = arreglo.reshape(2,5)
##si el contenido del arreglo no concuerda con la forma o viciversa da un error al momento de compitar como est e al hacer un shape
##con 2 arreglos de 5

print(arregloReshape)