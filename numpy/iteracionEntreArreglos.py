import numpy as np

arreglo = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arreglo)

##cuando se hacen arreglo multidimensionales deben usarse ciclos anindados ya que el contenido se encuentra denotro de otro arrelgo
##ciclo aninadado
for i in arreglo: ##entramosa la arreglo
    for j in i: ##recorremos arreglo del arreglo
        print(j) ##se imprime el contenido