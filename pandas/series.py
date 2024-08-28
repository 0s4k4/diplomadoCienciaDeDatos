import pandas as pd

dias = [10,28,31,30]

meses=pd.Series(dias,index = {"Enero","Febrero","marzo","abril"})

print(meses)