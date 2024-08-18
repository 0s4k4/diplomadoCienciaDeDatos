import csv  ##importasmos al libreria csv

##se abre el archivo csv y se le da el nombre file
with open('equipoPokemon.csv') as file:
    reader = csv.reader(file) ##se lee el csv 
    
    for row in reader: ##iteramos con la variable row
        print (row) ##se imprime el archivo 