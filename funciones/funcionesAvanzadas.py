##funciones con parametros 

def saludo(nombre):
    print(f'Holaa soy {nombre} ')
    
def sumarNumeros(*args):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado
##con esta funcion podemos crear una suma de una variable que tenga una longitud
##con args nos permite aceptar cualquier cantidad de argumentos y crea una tupla donde se almacenan  
# nombre = input('introduce tu nombre ')
# saludo(nombre)

###funcion con longitud 
print(sumarNumeros(1,2,3,4,5,1))

