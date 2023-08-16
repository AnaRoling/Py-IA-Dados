# o que estiver dentro do dicionario deve ser uma chave unica
 
#customer = {
  #  "nome": "John Smith",
 #"age": 30,
   # "is_verified": True
#}
#print(customer["nome"])#retorna o valor corespondente da chave
#customer["nome"]="Ana"#atualiza
#customer["niver"]="18/06"#atualiza
#print(customer.get("jcjk","jan 1"))#se a chave não existir retorna none e pode ser especificado uma resposta

#tradutor de numeros 
numeros= {
   '1': "um",
    '2': "dois",
    '3':"tres",
    '4':"quatro"
}
output = ""
telefone= input("Telefone: ")
for num in telefone:
    output += numeros.get(num,"!") + "  "
print(output)
