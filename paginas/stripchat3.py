import requests
import json

def cargarDatosStripchat3(dia,mes,año,dia2,mes2,año2,db):

    print('Estadisticas Stripchat')
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    

    cookies = {
        'stripchat_com_firstVisit': '2023-03-22T19%3A09%3A18Z',
        'guestWatchHistoryIds': '',
        'guestFavoriteIds': '',
        'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22bzs9JfX8zJNqIQFfNqXXu6%22%2C%22session_id%22%3A1680363384926%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
        'alreadyVisited': '1',
        'amp_19a233': 'bzs9JfX8zJNqIQFfNqXXu6.MTA4MjMzNjkx..1gsuncs2u.1gsuq5t2r.0.4a.4a',
        'isVisitorsAgreementAccepted': '1',
        'sCashGuestId': '5ef59394036cb1887c6eb7f4c70a93d3a7903546a2887c626e0a567b984a25aa',
        '_ga': 'GA1.1.1379988165.1679512158',
        '_gid': 'GA1.2.180793273.1680363386',
        'stripchat_com_sessionId': '8c2b28af15673f1eb4f616c84ce7f5ff6d949d2a2ccec2fe750a733ef3d4',
        'stripchat_com_sessionRemember': '1',
        'userWatchHistoryIds': '',
        'intercom-session-ylooj7fw': 'T2NNTXJhcllsME9GaHNndFVReFhLVERrQy9MdldHSlE5cUNwRXJOdW5sYmhYMWtsSTFsb0NBcFhPd1ducDJPdC0tek5TTjJSQ0plWVRMSzBYNC9PZnQwZz09--607a11795bca5e6b22659776ddfd1a2336f34f24',
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

    response = requests.get('https://es.stripchat.com/api/front/users/108233691/earnings?from='+año+'-'+mes+'-'+dia+'T05%3A00%3A00Z&until='+año2+'-'+mes2+'-'+dia2+'T04%3A59%3A59Z&uniq=7htn1dkp4cxqv36w', headers=headers, cookies=cookies)

    eq = json.loads(response.text)
    print(eq)

    for i in range (0, len(eq['earnings'])):
        db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
    
 