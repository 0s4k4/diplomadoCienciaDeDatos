##La condicionalIF nos ayuda a tomar una desicion segun la condicion 
##ejemplo

x = 0
y = 4


if x < y:  #indica que si x es menor a y se ejecuta la sentencia
    print("x es menor a y")
    
    
print('**** ejecucion de bloque de sentencias **** ')
##se desea evaluar una condicion y luego hacer mas una cosa si es verdadera
###si hace buen tiempo cortar cesped, desebar el jardin, sacar el perro a pesear
estado_tiempo = False ##establecemos si es false o true

if(estado_tiempo == True):   ##evaluamos la condicion y se muestra segun el estado si es true o false
    print('perfecto el estado de tiempo esta en perfectas condiciones')
    print('vamos a cortar cesped..')
    print('vamos a desberbar el jardin..')
    print('ahora vamos a sacar al perro a pasear...')
    print('listo..')
else:
    print('oh no hay buen clima mejor vamos a dejarlo para otro dia')