
f = open('numeros.txt','r') ### abrimos el archivo de los numeros con el nombre del archivo y parametro r
sumatoria = 0 ##establecemos la sumatoria en  0

for linea in f : #para linea  in f que es la lectura del archivo
    linea = linea.strip() #con strip eliminamos los saltos de linea
    numero = int(linea) #numero es igual a integer de la linea donde se encuentra el texto que son numeros del archivo de txt numeros
    sumatoria += numero ##sumatoria es igual y mas a numero 
    
##print(sumatoria) ### se la sumatoria de sumatoria
