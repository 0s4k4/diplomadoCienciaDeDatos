##un ciclo o iteracion con un rango de numeros de inicio y finales

### for(!=1; inicion, i <= 10; dondicion, i++ ; decremento)
##ciclo for se utiliza sobre una lista de elementos deuna forma tal como cada iteracion, se puede ejecutar la misma accion
##sobre cada uno de los elementos de una lista
mi_lista = ['juan',"antonio","pedro","ana"]

for elemento in mi_lista:
    print(elemento)
    

##estos son elementos iterables
lista = ['foo','bar','baz']
tupla = ('foo','bar','baz')
set = {'foo','bar','baz'}
diccionario = {'foo':1,'bar':2,'baz':3}


print(type(lista))
print(type(tupla))
print(type(set))
print(type(diccionario))


print('***** iteraciones **** ')
for mi_tupla in tupla:
    print(mi_tupla)

for clave in diccionario:
    valor = diccionario[clave]
    print(f"Clave: {clave}, Valor: {valor}")
    
    
    
