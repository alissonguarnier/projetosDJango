import requests
url = 'http://localhost:8000/api/autores/'		# URL do endpoint de autores
token = 'b01fc0f1d21f5854317a6dc6ba7b2b90f28589ff'	# Token de autenticação

data = {								# Dados do novo autor
   'nome': 'Jô Soares'
}

headers = {								# Cabeçalhos da requisição
   'Authorization': f'Token {token}',
   'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers) # Envia o POST

if response.status_code == 201:					# Verifica o resultado
   print('Autor criado com sucesso:', response.json())
else:
   print('Erro ao criar autor:', response.status_code, response.text)