import random 

with open('numeros2.txt','w') as file:
     
     for _ in range(100):
         file.write(f"{random.randint(1, 100)}\n")
