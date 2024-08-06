a = True 
b = False

### resulta true si ambos o los demas son true, si no son false
print('**********operador and**********')
print(a and a)
print(a and b)
print(b and a)
print(b and b)


##OPERADOR OR, sale true si algunos es true
print('**********operador or**********')
print(a or b);
print(a or a);
print(b or b);
print(b or a);

##operador not, da como resultado true si  y solo si su argumento es false
print('**********operador not**********')
print (not a);
print (not b);

print('**********Expresiones computestas**********')
##expresiones compuestas
##python evalua primero not, luego and y al final los or
print((not a) and b)
##evalua a 'False' por que ´(not a)´ es false  y b es false, por lo cual es false segun la logica de and
##Salida FALSE
print(not (a and b))
## Evalua true por que  a and b es false y not nos invierte este resultado dado TRUE
##SALIDA true

print(not b or a)
##evalua not b que invierte b de false a true, y al evaluar or con a al ser true resulta ser true
##por lo cual su salida es TRUE

print((not b) or a)

##evalua lo siguiente
#not b nos da como resultado true  al revertir el false a true
##a es true, lo cual es true or true

print(not(a or b))
 #evalua a or b, lo cual da como resultado true
 #pero al revetir el true nos da false
 
print("******expresiones compuestas con or y and******")
print(b and a or b)
##se evalua primero and segun la prioridad
#b and a da false
#false or false da salida false
print((b and a) or a)
## da un true por que false y true da false pero false y true da un true
print(b and (a or a))
##da un false por que b que es false compara and con a y a es true

print(a or a and b)
#da true por que a and b da false pero a y false da true
print((a or a) and b)
#da false por que b false y a or a es true da como resultado false por el and
print(a or (a and b))
#da como resultado true como a y b es false y or a da false or true osea es true
