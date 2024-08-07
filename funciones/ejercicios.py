##RETOS DE FUNCIONES

#1
##Escribir una funcion que solicite por separado los nombres y apellidos de una persona
##, estos se deben guardar en variables separadas. Posteriormente concatenar ambos valores 
#e imprimir el nombre completo

def nombreCompleto(nombre,apellidoP,apellidoM):
    print(f"El nombre completo de la persona es {nombre} {apellidoP} {apellidoM}")

nombre = input('Nombre completo de la persona: ')
apellidoP = input('Apellido paterno de la persona: ')
apellidoM = input('Apellido materno de la persona: ')

nombreCompleto(nombre,apellidoP,apellidoM)

#2
#Crear funcion que calcule el promedio de los siguientes valores, 10,20,30,40,50 
# e imprimir el resultado

def promedioLista(lista_promedio):
    
    print(sum(lista_promedio)/len(lista_promedio))
    


lista_promedio = [10,20,30,40,50]

promedioLista(lista_promedio)


#3 
#Crear funcion que calcule la velocidad y la imprima en pantalla, la funcion recibira dos parametros
#la distancia que se recorre y el tiempo que consume para recorrer esa distancia

##la formula es la siguiente
##velocidad  = distancia/tiempo
def calculoVelocidad(distancia,tiempo):
    velocidad = int(distancia)/int(tiempo)
    
    return velocidad

distancia =  input('ingresa la distancia ')
tiempo = input('Ingresa el tiempo ')

velocidad  = calculoVelocidad(distancia,tiempo)

print(f"la velocidad es  {velocidad}")
##4
##crear una funcion que de acuerdo a la edad  de una persona determine si puede o no votar en las 
##elecciones del 2024, debe recibir la edad como parametro y realizar la condicion
# e imprimir el resultado


def mayoriadeEdad(edad):
    edad = int(edad)
    
    if(edad >= 18):
        print(f'puede votar por ser mayor de edad, ya que su edad es {edad}')
    else:
        print(f'no puede votar por que no es mayor de edad, ya que su edad es {edad}')
    

edad = input('Ingresa tu edad ')

mayoriadeEdad(edad)


