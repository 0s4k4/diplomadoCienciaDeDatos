import numpy as np 

arreglo = np.array([2,4,6,8,10,12,14])
#se crea un arreglo 


print(arreglo[1:4])

##se especifica cuales arreglos se va a devolver, en este caso del indice 1,2,3 (entre el 1 al 4 no se incluyte el 4)
##se muestra el 4,6 ,8

##a esto le llamamos arrelg unidimencional con parametros explicitos, ya que le damos de onde iniciar y donde terminal

arreglo2 = np.array([2,4,6,8,10,12,14])


print(arreglo2[::2])
##en esta declaracion se inica desde 0 por que no hay inidice inicial,  se salta de dos en dos dando como resultado 0 salta a 2 e imprime 2 salta a 4 e imprime, 4 salta a 6 e impriome 6 salta a 10 e imprime 10 salta a 14 e imprime
##a esta declaracioon se le llama declaraciom implicita

