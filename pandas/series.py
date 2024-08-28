import pandas as pd ##se establece pd como alias de pandas

versionesPokemon = ["Red and green","Gold and Silver","Ruby and Shapirre","Diaomond and pearl"]
##lista contiene los datos que se agregara a la serie
consola = pd.Series(versionesPokemon,index=["Gameboy","Gameboy color","Gameboy Advance","Nintendo DS"])
##usando index podemos designar nuestras propias labels, por omision estas seran numeros del 0 en adelante
#se muestra dataframe en la pantalla
print(consola)
