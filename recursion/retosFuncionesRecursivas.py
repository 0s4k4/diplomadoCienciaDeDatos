##crear funcion recursiva que permita imprimir los valores de  1 a n orden ancendente.
#por ejemplo  si  mi funcion tiene  como nombre imprimir  y mandar a llamar  con un argumento
#numerico iguala  5  entonces que imprima  los valores 12,3,4,5
import random 
def imprimir(n):
    # Condición base: si n es 1, imprime 1
    if n == 1:
        print(1)
    else:
        # Llamada recursiva con n-1
        imprimir(n - 1)
        # Imprime el valor actual de n
        print(n)

# Ejemplo de uso
#imprimir(5)


##crear  una funcion recursiva que permita adivinar un numero del 1 al 10. la funcion se debe 
# llamar asi misma  hasta que el usuario adivine el numero aleatorio. El numero por adivinar 
#puede ser generado de manera aleatoria, el usuario debe capturar un valor numerico
#el cual  se comparara con el numero generado aleatoriamente




def adivinar(y, numeroAleatoria = None):
    
    
    if numeroAleatoria is None:
        
        numeroAleatoria = random.randint(0, 10)
    
    if y == numeroAleatoria:
        print(f'numero correcto, numero generado {numeroAleatoria}, numero ingresado {y}')

    else :
        print(f'numero equivocado, numero generado {numeroAleatoria}, numero ingresado {y}')
        adivinar(y)

adivinar(4)