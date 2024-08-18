#son colecciones de datos con la estructura llave-valor con el {} o dict()

persona = {'nombre':'tasuya','edad':13}

print(persona) ## se imprime el contenido completo del diccionario

print(persona['nombre']) ##se accede al diccionario, y se imprime el contenido de la llave nombre

print(persona.get('ss')) ##similar al anterior metodo, pero la diferencia, si encuentra un error, da el mensaje none y no un mensaje de error como el anterior


persona['telefono'] = '234134'
##llave                 ##valor
persona['colores'] = ['verde','morado','naranja']
print(persona) ##en este caso agregamos una lista y un dato normal a nuestro diccionario'

persona['nombre'] = 'makoto'
persona['edad'] = 15
### para actualizar nuestro valor, es simple solo se invoca la llave, y se vuelve asignar el nombre
print(persona)

##eliminar elementos

del persona['colores'];

print(persona) ##se elimina con la frase del luego el diccionario y la llave

persona.pop('edad')

print(persona) ##con esto, se elimina usando el metodo pop y el parametro se ingresa la llave que se desea eliminar

# persona.clear() ##con el clear, se elimina el contenido del diccionario
# print(persona)

# del persona 

# print(persona) ##o tambien podemos eliminar todo el diccionario, con el del, y al volverlo invocar da el error al imprimir por que se elimina por completo

print('items',list(persona.items())) ##imprime el valor y llave por cada valor 
print('Keys',list(persona.keys())) ##imprime la llave del diccionario
print('values',list(persona.values())) ##imprime el valor de cada llave

##metodos integrados dentro en diccionarios

PecadosCapitales = {'dragon':'meliodas','serpiente':'diane','oso':'king','carnero':'gowther','jabali':'merlin','leon':'escanor'}
##definimos un diccionario
for pecado in PecadosCapitales.keys(): #ciclo for donde pecado sea las llaves del diccionario de pecados capitales
    
    #imprime la llave de pecadosCaitales y ese obtiene e imprime el valor de la llave de pecados capitales
    print(f"El pecado capital de {pecado} es {PecadosCapitales.get(pecado)}") 
