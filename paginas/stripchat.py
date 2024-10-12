import requests
import json

def cargarDatosStripchat(dia,mes,año,dia2,mes2,año2,db):

    print('Estadisticas Stripchat')
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    

    cookies = {
        'stripchat_com_firstVisit': '2023-04-16T14%3A40%3A49Z',
        'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%221P9jHk2FjsHl_WPoF-K9SG%22%2C%22session_id%22%3A1682341128928%2C%22up%22%3A%7B%22page%22%3A%22index%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
        'alreadyVisited': '1',
        'amp_19a233': '1P9jHk2FjsHl_WPoF-K9SG.NDY1MDYxMQ==..1guplgqn0.1gupm4crp.0.70.70',
        'isVisitorsAgreementAccepted': '1',
        '_ga': 'GA1.2.1301892351.1681656050',
        '_gid': 'GA1.2.573934947.1682341133',
        'stripchat_com_sessionId': 'e15cb182ba0c3dac70581619b04f532c7af963b6f35ffa5d3a907fa94e84',
        'stripchat_com_sessionRemember': '1',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json',
        'Front-Version': '10.11.13',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Referer': 'https://es.stripchat.com/studio-earnings',
        'Connection': 'keep-alive',
        'TE': 'trailers',
    }

    params = {
        
        'from': ''+año+'-'+mes+'-'+dia+'T05:00:00Z',
        'until': año2+'-'+mes2+'-'+dia2+'T04:59:59Z',
        'uniq': '1tkzc5a6jmiv0nhy',
    }

    response = requests.get('https://es.stripchat.com/api/front/users/4650611/earnings', headers=headers, cookies=cookies, params=params)

    eq = json.loads(response.text)
    print(eq)
    
    for i in range (0, len(eq['earnings'])):
        db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
    
 