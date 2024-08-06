##tipos de datos
##existen diferentes de tipos de datos en python

numerosInteros = 9;
numerosReales = 1.2;
cadenasTexto = 'assasd';
numComplejo = 1.2-1j

print('****** funcion type nos obtiene el tipo de datos de las variables ****** ')
###con trype obtenemos el tipo de datos
print(type(numerosInteros))
print(type(numerosReales))
print(type(cadenasTexto))
print(type(numComplejo))
print('****** funcion id nos obtiene el id asignado en la memoria ****** ')
print(id(numComplejo))

print('**** cadenas de caracteres ****')

j = 6
texto = 'j = ' + str(j)
print(texto)
##convettimos el tipo de datos de int a txto y se concatena

w =6
texto2 = "\"j= "+ str(w) + "\""
print(texto2)
