import requests

response= requests.get('https://www.folha.uol.com.br/')
print('Status code',response.status_code)
print('Header')
print(response.headers)

print('\n content')
print(response.content)
