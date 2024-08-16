##es una estructura que nos ayuda a almacenar muchos valores en una variable, estos se 
#encierran en  [] y se separan por comas, es mutable osea que se puede editar, eliminar y agregar

##ejemplo de una lista

mi_lista = [1,2,3,4,5]

#print(mi_lista)  ## se imprime la lista

#print(mi_lista[-1]) ##accedemos al elemento, si ponemos -1 accedemos al ultimo elemento

##manipulacion de los elementos
mi_lista[0] = 10 ##ponemos la posicion 0 como 10

#print(mi_lista)


mi_lista.append(6)

#print(mi_lista) ##agregamso el valor 6 con append y imprimimos

##operaciones con la lista


##index
#print(mi_lista.index(50)) 
##devolvemos la ubicacion del elemento buscado, si el elemento no se encuentea en la lista
#arroja un error.

lista2 = [1,2,[2,3]]
##lista dentro de otra lista

lista2Tamali = len(lista2);
##print(lista2Tamali) ##obteneos el tamaño de la lista con la funcion len
#print(mi_lista)
mi_lista.pop(1)
#print(mi_lista) ## con la funcion pop eliminamos un elemento invocando su funcion y como parametro
#usamos la posicion del elemento
#print(mi_lista.clear())  ##con esta funcion se limpia el contenido de la lista

mi_lista.extend(lista2) 
#print(mi_lista)
##combinamos dos listas con esta funcion  de extendr dando como parametro la lista que se dese agregar

lista = ["uno", "dos", "tres"]
lista3 = ["cuatro", "cinco", "seis"]
#lista.extend(lista3)
#print(lista)


##operaciones basicas

#print(lista.count('siete'))
##con la funcion count contamos las veces que aparece un elemento en nuestra lista, si no aparece devuelve un cero

lista.insert(3,'diez')
print(lista)
## con la funcion insert, le damos el parametro de  dentro de intert que corresponde a la
#posicion y luego al elemento que se va insertar

lista.remove('diez') #esta funcion nos ayuda a eliminar un ejemplo, dando como parametro el texto
#o elemento a remover
print(lista)

lista.reverse()
print(lista)
##REVERSE se usa para invertir el orden de una lista

lista.sort()
print(lista)

#sort es un metodo para ordenarlos de la manera mas ascendete posible
