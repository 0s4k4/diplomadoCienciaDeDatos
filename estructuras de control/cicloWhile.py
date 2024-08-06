##ciclo while
# while <expresion> : 
#   sentencia representa lo que se ejecuta si se cumple el while

## donde se encuentra el while se evalua una expresion en un contexto booleando, si es true s eejecuta el cuerpo , 
#si se vuelve false el programa continua  en la primera declaracion luego del cuerpo del while
n = 5  ##se establece el  valor

while n > 0: ##evaluamos la expresion que es n mayor a 0
    n -= 1  ##cuerpo, menos igual a -1
    print(n) ## se imprime n

##al finalizar la iteracion, nos da esta impresion con el valor de n
print(f'ahora n es menor a 0, el valor de n ahora es {n}')