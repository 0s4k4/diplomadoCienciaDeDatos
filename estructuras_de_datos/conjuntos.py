##conjuntos, estructura que nos permite almacenar y manipular colecciones de datos, similares a los diccionarios pero para diferentes casos de uso
#es una coleccion no ordenada dse elementos unicos son creados usando las lleves {} o con la funcion set()
##puede contener un numero ilimitado de categorias entre ellas entero, flotante, tupla,cadena,etc
##ejemplo de conjunto 
numeros = {1,2,3,4}

print(type(numeros))  ##nus imprime que es un tipo de estructura set o conjunto 

numeros2 = {1,2,2,3}
print(numeros2)  ##imprime pero como hay dos repetidos, omite uno

##un conjunto no puede  tener elmentos mutblaes como listas,conjunto o diccionarios

## diccionario de numeros enteros
numeros_enteros = {10,20,30,50}
print(numeros_enteros)

##conjunto de valores mixtos
valores_mixtos = {1,'hola',(10,20,30)}
print(valores_mixtos)

conjunto =  {1,2,3,4,1,3,4,2}

print(conjunto) ##me imprime solo los valores unicos

listaNumeros = [1,2,3,4,5,6,7,8,9]

conjunto_lista = set(listaNumeros)

print(conjunto_lista)  ##se convierte una lista en un conjunto con la funcion de set

##agregar elementos a un conjunto

numeros3 = {1,2,3,4}

numeros3.add(6)

print(numeros3)

numeros3.update([7,8]) ##con update mediante  datos en una lista le anadimos mas datos en una sola linea

print(numeros3)

##eliminar datos de mi conjuntos
##con remove le damos en el parametro el elemento que deseamos eliminar, si no se encuentra envia un mensaje de alerta
#con discard no hace nada al respecto

# numeros3.remove(10)
# print(numeros3)  ## como no tiene el numero 10 nuestro conjunto, lanza un error

# numeros3.remove(4)
# print(numeros3)  ## como no tiene el numero 10 nuestro conjunto, lanza un error

 
numeros3.discard(4)  ##  el elemento no se encuentra en los conjuntos pero no muestra ningun error solo lo ignora
print(numeros3) 

##iteracion sobre un conjunto

estados = {'Guanajuato','Michoacan','Jalisco','Veracruz','Sonora','Puebla','Durango'}
for estado in estados:
    print(estado)

##se puede imprimir los elementos de una conjunto en una iteracion e imprimir los resultados dentro del conjunto
#aunque al ser una lista sin orden no tiene ningun orden en especial

##OPERACIONES CON CONJUNTOS

##los conjuntos  son una coleccioon de elementos unicos y no ordenados de los cuales se puedes pueden ejecutar
#una serie de operaciones como union,interseccion y diferencisa

numero1 = {1,2,3}
numero2 = {4,5,6,1}

numeros4 = numero1.union(numero2)
print(numeros4)  ##operacion de union de dos diferentes colecciones de conjuntos
numerosInterseccion = numero1.intersection(numero2)
print(numerosInterseccion) ##nos arroja la interseccion de ambos conjuntos, si le agrego un uno a mi segundo conjunto me arroja un 1 por que 
#lo tiene en comun
numerosDiferencia = numero2.difference(numero1)
print(numerosDiferencia)  ###nos arroja la diferencia entre los dos conjuntos, en este caso nos da la diferencia del numero2 al numero 1
#y es 4,5,6

##union de conjuntos

A = {'rojo','verde','azul'}
B = {'amarillo','rojo','naranja'}

print(A|B)  ##se la union de los dos conjuntos
print(A & B )  ##se imprime lo unico que tienen en comun osea su interseccion que es rojo
print(A - B) ##se imprime su diferencia osea verde y azul, osea lo que no esta en el otro conjunto