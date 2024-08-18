import csv  ### se imprime el csv

equipoPokemon = [  ##creamos una lista donde definimos primero la cabecera de mi csv
        
        ["Pokemon","lvl","Tipo/s"],
        ['Articuno','10',"volador/hielo"],
        ["Greeninja","34","agua/obscuro"],
        ["Charizard","36","Fuego/volador"],
        ["Pikachu","40","Electrico"],
        ["Gengar","50","Veneno/Fantasma"]
    ]

with open('equipoPokemon.csv',"w",newline="") as file: ##abrimos el archivo csv y lo nombramos como file
    writer = csv.writer(file) ## escribimoos el contenido al csv
    writer.writerows(equipoPokemon) ## escrbimos cada columna en el csv 


