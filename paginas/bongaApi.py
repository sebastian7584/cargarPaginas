import requests

def datosBonga(año,mes,dia,modelo):
    headers = {
        'ACCESS-KEY': 'szgufgredm7vuoan5qink73qu6',
    }
    fecha= año+'-'+mes+'-'+dia
    params = (
        ('username', modelo),
        ('date_from', fecha),
        ('date_to', fecha),
    )

    response = requests.get('https://bongacams.com/api/v1/stats/model-regular-earnings', headers=headers, params=params)

    #NB. Original query string below. It seems impossible to parse and
    #reproduce query strings 100% accurately so the one below is given
    #in case the reproduced version is not "correct".
    # response = requests.get('https://bongacams.com/api/v1/stats/model-regular-earnings?username=YOUR_MODEL_USERNAME&date_from=2020-04-01&date_to=2020-04-30', headers=headers)

    data = response.json()
    return data