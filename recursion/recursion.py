##es una funcion que se llama asi misma , es posuble
#que un bloque de instrucciones ejecute cierta cantidad de veces
#remplazando instruciones repetitivas
#es util para resolver problemas complejos que se pueden resolver
##diviendo en problemas mas pequeños
##si dentro de la funcion encontramos una funcion que existe una llaamda
#a si misma , entonces  decimos que es una funcion  recursiva

def factorial(x):
    if x== 0:
        return 1 ##si x es igual a 0, nos devuelve un 1, en caso de no tenerlo, se presentaria el error de overflow en la memoria
    ##se basa en la expresion matematica 0!=1
    else:
        ##si x no es 0, la funcion retorna el producto x y el factorial x -1
        ##esto nos permite que la funcion que se llame a si misma con un valor de x reducido en 1
        #la recursion continua hasta que x llegue a 0, momento en la funcion comienza a resolver  y retomar valores
        return x * factorial(x-1)
    
print(factorial(0))
##ejemplo factorial(1)  = 1*1 = 1 debido a que entra en el return de 0
print(factorial(5))
##ejemplo factorial(5) 
##se llama factorial x con x = 5
#como x no es igual a 0 se ejecuta  la llamada recursiva  return  x * factorial(x-1) es decir
#5 * factorial(4)
##se empiezan a resolver 
#factorial 1 = 1 * 1 = 1
#factorial 2  = 2 *1 = 2
#factorial 3  = 3 * 2 = 6
#factorial 4 = 4 * 6 = 24
#factorial 5  = 5 * 24 = 120
print(factorial(10))
    