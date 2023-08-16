# Exemplo
# Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuario 

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome= input('Qual produto você deseja pesquisar? ')

#print(url_base + produto)
response = requests.get(url_base + produto_nome)

site= BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core ui-search-result--advertisement andes-card--padding-default andes-card--animated'})
for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    simbolo = produto.find('span', attrs={'class': 'price-tag-symbol'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})

    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    if(centavos):
        
        preco_completo = f'Preço: {simbolo.text} {real.text},{centavos.text}'
    
    else:
         
         preco_completo = f'Preço: {simbolo.text} {real.text}'

    lista_produtos.append([titulo.text, link['href'], preco_completo ])


todos_produtos = pd.DataFrame(lista_produtos, columns=['Titulo', 'Link', 'Preço'])

print(todos_produtos)
    #print('Titulo do produto: ', titulo.text)
    #print('Link do produto: ', link['href'])
    #print(f'Preço: {simbolo.text} {real.text},{centavos.text}')



