###una cadena es una estructura que  no se puede descomponer en partes mas primnitivas, esta compuesta por varios datos
#es una secuencia de ceros o mas caracteres, puede ser representada con comillas simples o dobles
#la posicion de los caracteres se numeran dede 0 a la izquierda, hasta la longitud sea menos de 1 ala derecha, 
#por ejemplo tecnologisa tiene 11 caracteres iniciando con 0 y terminando en el 10

##operador subincide
##en una cadena se puede acceder a un dato del string poninedo el string en una variable y un operador subindice

texto1 = 'hola';

# print(len(texto1)) ##con len se imprime la longitud de mi cadena
# print(texto1[0]) ###con 0 se imprime el caracter de mi posicion 0
# print(texto1[-1]) ###con -1 se imprime el caracter de mi posicion -1 que sea el 4

##iteracion con mi cadena

for index  in  range(len(texto1)): ##definimos primero nuestra iteracion con un index, index recorre el lango de la longitud de la iteracion
    print(index,texto1[index]) ## se imprime el index y luego con texto1[index] se imprime el caracter de la posicion 
    

##el slicing se aplicaca cuando queremos extraer porciones de cadenas llamadas subcadenas
pokemon1 = 'squirtle'
nombrePokemon = pokemon1[0:]  ##accede al nombre del pokemon, dando el slicing del caracter 0 al ultimo por que no se le indico rango en cual terminal

print(nombrePokemon)

primeraLetraPokemon = pokemon1[0:1]
print(primeraLetraPokemon)  ##se imprime la primera letra del nombre del pokemon

nommbrePokemonv2 = pokemon1[:len(pokemon1)]
print(nommbrePokemonv2)  ##este slicin lo imprime completo por que se esta dando toda la longitud completa del texto que es 8, iguala 0: o :

pokemonRangoLetras = pokemon1[0:5]
print(pokemonRangoLetras) ##imprime el rango del 0 al 5, osea  s q u i r 

pokemonUltimaLetras = pokemon1[-1:]
print(pokemonUltimaLetras)  ## me imprime la ultima letra osea el e dando el parametro de -1 que se tradue al ultimo y no estableciendo fin hasta que termine y como termina en esa, se queda hasta ahi, lo mismo si pusieramos hasta el 7

pokemonUltimaLetras = pokemon1[7:]
print(pokemonUltimaLetras)

##METODOS DE CADENAS
#ES COMO UNA FUNCION PEERO CON UNA SINTAXIS DIFERENTE, LLAMA A UN METODO CON UN VALOR DE DSTOS DADO LLAMADO AL OBJETO QUE SE COLOCA ANTES DEL NOMBRE DEL METODO EN LA LLAMADA
#LA SINTAXIS ES ASI OBJETO.NOMBRE_DEL_METODO(ARGUMENTO)
##EL METODO ESPERA ARGUMENTOS Y DEVUELVE VALORES
# EL METODO CONOCE EL ESTADO INTERNO DEL OBJETO CON EL QUE SE LLAMA

##ALGUNOS DE LOS METODOS PARA CADENAS

##PARA CALCULAR NUESTRA LONGITUD
nombreCiudad = 'Pueblo Paleta'

longitudNombreC = len(nombreCiudad)

print(longitudNombreC)

cuantasA_tien_la_ciudad = nombreCiudad.count('a')
print(cuantasA_tien_la_ciudad)  ##cuenta la cantidad de a que tiene la ciudad

terminaConTa = nombreCiudad.endswith('ta')
print(terminaConTa) ##verifica con endswitch con que palabra termina nuestro string, si coincide con el valor del metodo, da true sino un false

empiezaLetre = nombreCiudad.startswith('p') 
print(empiezaLetre) ##verifica si on startswitch si la palabra con la que inicia coincide o no

##tanto start como endswitch toman en cuenta si son mayusculas o minisuculas

encontrarLetraPalabra = nombreCiudad.find('u')
print(encontrarLetraPalabra)  ## con el metodo find, nos ayuda a darnos la posicion donde se ubica la letra o palabra, si es palabra, da desde donde inicia

esAlfanumerico = nombreCiudad.isalpha()
print(esAlfanumerico)  ##nos verifica si nuestra cadena es alfanumerico o no

print("Nidoran".isalpha()) ###da true por por que si es alfanumerico

print("69".isalnum())
print("69".isdigit())  ##estos dos nos indican si son digitos y numeros


palabras = ['hola','mundo','soy','yo'] ##lista de las palabras
frase = " ".join(palabras) ## se junta con join y se le puede dar que ponerse entre los elementos de la lista, puede ser un espacio en blanco 

print(frase)

nombreMangaka = 'Akira'

print(nombreMangaka.upper()) ##con uppper toda la cadena se hace en mayuscula
print(nombreMangaka.lower()) ##con lowst toda la cadena se hace minuscula
print(nombreMangaka.replace('a','e'))  ## con replace, se remplaza el primer parametro con el segun dentro del metodo
#akira pasa a akire