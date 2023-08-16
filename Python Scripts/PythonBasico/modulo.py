#import converters
#from converters import kg_to_lbs  
#kg_to_lbs (100)
#print(converters.kg_to_lbs(70))

#import converters
#from converters import find_max
#numbers = [10,3,6,2]
#maximum=find_max(numbers)
#print(maximum)

import random

#primeiro programa
#random() gera um valor valido de 0 to 1
# print(random.randint(10,20)) gera valores nesse intervalo 
#for i in range(3):
#print(random.randint(10,20))

#segundo programa

menbers = [ 'John','Mary','Bob',"Mosh"]
leader=random.choice(menbers)
print(leader)



from pathlib import Path

path = Path ("ecommerce")
print(path.mkdir())#cria diretorio 







