##contujos de elementos ordenados, como diferencia estas no pueden ser modificadas una vez creadas
##se crean apartir de parentesis

mi_tupla = (1,2,3)
print(type(mi_tupla))
##esto nos imprime que es un tipo de dato llaamda tupla

print(mi_tupla)

##funcion tuple

t = tuple({1,2,3})
print(t) ##convertimos una lista en una tupla con la clase tuple, dando 
#como parametro los elementos en formato de lista

tu = tuple("hello")
print(tu)  ##en este ejemplo hacemos una tupla apartir de un texto

##acceder a las tuplas

tp = (1,2,4,5)

print(tp[0])
print(tp[-1])
print(tp[1:3])

##el primero accedemos con el indice, se devuelve 1
##el segundo accedemos al utlimo osea 5 con el -1
##el ultimo accdemos al rango del 1 al 3, lo cual nos devuelve 2,4

##OPERACIONES CON PYTHON
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2 ##operacion de crear una tupla apartir de la suma de dos
print(t3) 

t4 = t1 * 3
print(t4)  ##multiplicamos los resultados de la tupla por 3
