#numbers = [1,10,33,100,2]
#maior=numbers[0]
#for  x in numbers:
   # if x > maior:
    #  maior = x 
#print(maior)


#metodo append() adiciona o () no final da lista
#metodo insert(0,0) index , numero (add na posicao do index)
#metodo remove(0) remove um elemento da lista
#metodo clear esvazia a lista
#pop remove o ultimo elemento da lisa
# index retonar o index do elemeto da lista 
# utilizando (50 in numbers) podemos saber se 50 está na lista com o retono de um valor boealno
#number.count()retorna a quantidade de elemento identicos ao valor passado
#resposta nome representa a falta de valores validos 
# 
#numbers = [5,2,1,7,4]
#numbers2= numbers.copy()
#numbers.append(10)
#print(numbers2)

lista = [1,1,2,2,3,3,4,4,5,5,6,7,8,9]
lista2= []
for list in lista:
    if list not in lista2:
        lista2.append(list)
print(lista2)






