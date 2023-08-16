import requests
from bs4 import BeautifulSoup

response= requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content,'html.parser')

#HTML da noticia 
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#titulo
#<a class="feed-post-link gui-color-primary gui-color-hover"
titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})

print (titulo.text)

#subtitulo 

 #<div class="feed-post-body-resumo" elementtiming="text-ssr">
  #STJ analisa pedido da Itália para que jogador cumpra pena no Brasil.
 #</div>
subtitulo = noticia.find('div', attrs={'classe': 'feed-post-body-resumo'})

print(subtitulo.text)


