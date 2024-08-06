nombre,edad = 'alejandra',27
##usando %
res1 = "Hola , %s tu edad es %s" %(nombre,edad)
print(res1)

##formantenado con str format
res2  = "Hola. {0} tu edad es {1}.".format(nombre,edad)
print(res2)

#usando F-STRINGS
res3 = f"Hola, {nombre} Tu edad es {edad}"
print(res3)

