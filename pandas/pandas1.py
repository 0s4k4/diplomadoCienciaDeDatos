import pandas as pd  ##se manda a llamar la lbreria

misPokemones = {
    ##coleccion donde  guardamos la informacion
    "Pokemon" : ["Pikachu","Sceptile","Greninja","Espeon","Articuno","Charmander"],
    ##en forma tabular, cada lista de datos repreenta una columna del dataframe
    "Tipo/Tipos":["Electrico","Hierva","Agua/Obscuro","Psiquito","Hielo/Volador","Fuego"],
    "Nivel":[60,50,80,40,80,10]

}

##se crea el dataframe y se asigna una variable
resultado = pd.DataFrame(misPokemones)


##se imprime en pantalla el dataframe
print(resultado)