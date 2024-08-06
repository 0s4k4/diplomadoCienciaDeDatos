##break termina de forma inmediata la iteracion del while por completo
#saltara a la siguiente linea de la intruccion que sigue luego del cuerpo del ciclo
## termina la iteracion del ciclo actual y saltar a la parte superior del ciclo y la expresion se vuelve a evaluar, se reinicia el ciclo para ver si sigue



n = 5
##evaluamos n
while ( n > 0 ): #al ser mayor a 0 inicia
    n -=1
    if n  == 2: ##si es igual a 2, se hace un break
        break
    print(n)
print('ciclo terminado')


###clausa else

print('********* clausala else *********')
##else tiene la funcion solo si el ciclo se termina por  condicion false, si se sale con un breake no se ejecuta
m  = 5
while(m > 0):
    m -= 1
    print(m)
    
else :
    print('Ciclo terminado')