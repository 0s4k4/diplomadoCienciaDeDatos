# f = 5
# g = "hola"
# g = g+f
# print(g)
##este nos da error por que solo se puede concatenar str no int 

f = 5
g = 'Hola'
g = g+str(5)
print(g)
##ahora si se puede usar por que se convierte en un str