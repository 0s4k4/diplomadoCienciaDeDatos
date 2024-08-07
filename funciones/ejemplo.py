
##las funciones son bloques de codigo que ayudan a escribir menos 
##por lo cual podemos repetir el bloque solo invocando nuestra funcion

## hay de dos
##las que no cuentan con parametros
def saludo():
    nombre = input('Ingresa el nombre ')
    print(f"Hola {nombre}, gusto en saludarte. ")
    
saludo()


##que no esperan ningun parametro

##y las que si cuentan parametros
def saludo2(nombre):
    print(f"Hola {nombre}, un gusto bienvenido :)) ")
    

nombre2 = input("Holaaa ingresa tu nombre ")

saludo2(nombre2)

##que como se observa, esperan un parametro para poder ser ejecutas,
#y al momento de ser invocadas, se hace referencia al parametro
