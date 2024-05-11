import requests

# Definir el encabezado ACCESS-KEY
headers = {
    'ACCESS-KEY': '4gqwxrpj0gejtgsdfouyoege74pg'
}

# Definir el nombre de usuario del modelo
username = 'electrasex'

# Hacer la solicitud con los encabezados y el nombre de usuario especificados
response = requests.get(f'https://bongacams.com/api/v1/stats/model-regular-earnings?username={username}', headers=headers)

# Manejar la respuesta como lo necesites
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Response is not in valid JSON format")
else:
    print("Error:", response.status_code)
