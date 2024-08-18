import csv   ##importamos al biblioeta de csv

with open('equipoPokemon.csv') as file: ##abrimos nuestro csv con el objeto file
    obj = csv.DictReader(file) ## hacemos un objeto a nuestor csv 
    for item in obj: ##iteramos nuestro csv con item
        print(item['Pokemon']+' tiene un nivel de '+ item['lvl']+' y es de tipo '+item['Tipo/s'])
        ##hacemos un print donde invocamos header por header para imprimir lo correspondiente de cada row segun la iteracion dada
        