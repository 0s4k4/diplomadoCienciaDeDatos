### ==  es igual
## != disintigo
## < es menor
## <= es menor o igual
## > es mayor
## => es mayor o igual

print(5 > 2 and 5<3)
## 5 es mayor a 2 y 5 es menor a 3
## true y false da como salda false

print(5 > 2 and 5>3)
##si 5 es mayor a 2 y 5 es mayor a 3
## da true por que true and true es true

##utilizando la expresion or
print(5>2 or 5>3)
##nos da true por que 5 es mayor a dos es true or 5>3 que es true, nos da :
##true or true
print(5>2 or 5 > 6)
##nos da true por que 5 es mayor a 2 y  5 no es mayor a 6 pero al ser or, si una afirmacion es correcta da true

print(5>8 or 5>6)
##esta afirmacoon nos da false por que 5 no es mayor a 8 ni 5 es mayor a 6
##false

##ejeemplo de not en operadores de comparacion
print(5>8)
##no da un false por que 5 no es mayor a 8
not(5>8) 
##nos da un true por que invierte el false
print(5>2)
#nos da un true por que 5 si es mayor a dos
not(5>2)
#nos da un false por que 5 es mayor a dos pero invierte el not


