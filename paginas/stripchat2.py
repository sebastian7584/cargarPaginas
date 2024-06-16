import requests
import json

def cargarDatosStripchat2(dia,mes,año,dia2,mes2,año2,db):

    print('Estadisticas Stripchat2')
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    

    cookies = {
        'stripchat_com_firstVisit': '2022-04-11T05%3A54%3A46Z',
        'guestWatchHistoryIds': '30042591',
        'guestFavoriteIds': '',
        'baseAmpl': '%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22JPMfJl_A7RN_1SzE4UDCHU%22%2C%22session_id%22%3A1655395232266%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D',
        'alreadyVisited': '1',
        'amp_19a233': 'JPMfJl_A7RN_1SzE4UDCHU.NzM2NzI5NjE=..1g5mjtaga.1g5mk055r.0.15.15',
        '_ga': 'GA1.2.926580397.1649656482',
        'sCashGuestId': 'e7b61ffc8ecf759de18319f7ddcb71d95c7b86116843c3e95f63345614bd5e81',
        'isVisitorsAgreementAccepted': '1',
        'guestWatchHistoryStartDate': '2022-04-16T17%3A39%3A37.780Z',
        '__cflb': '02DiuFntVtrkFMde1dj4khwPfLgZByWZi5m3READjJSur',
        '_gid': 'GA1.2.1388636281.1655395233',
        'stripchat_com_sessionId': 'a6198f21a1bf98949dc7296739cf4cd65b099436268c3dac4955347f0a90',
        'stripchat_com_sessionRemember': '1',
        'userWatchHistoryIds': '30042591',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Front-Version': '10.34.13',
        'Alt-Used': 'es.stripchat.com',
        'Connection': 'keep-alive',
        'Referer': 'https://es.stripchat.com/studio-earnings',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'stripchat_com_firstVisit=2022-04-11T05%3A54%3A46Z; guestWatchHistoryIds=30042591; guestFavoriteIds=; baseAmpl=%7B%22platform%22%3A%22Web%22%2C%22device_id%22%3A%22JPMfJl_A7RN_1SzE4UDCHU%22%2C%22session_id%22%3A1655395232266%2C%22up%22%3A%7B%22page%22%3A%22other%22%2C%22navigationParams%22%3A%7B%22limit%22%3A60%2C%22offset%22%3A0%7D%7D%7D; alreadyVisited=1; amp_19a233=JPMfJl_A7RN_1SzE4UDCHU.NzM2NzI5NjE=..1g5mjtaga.1g5mk055r.0.15.15; _ga=GA1.2.926580397.1649656482; sCashGuestId=e7b61ffc8ecf759de18319f7ddcb71d95c7b86116843c3e95f63345614bd5e81; isVisitorsAgreementAccepted=1; guestWatchHistoryStartDate=2022-04-16T17%3A39%3A37.780Z; __cflb=02DiuFntVtrkFMde1dj4khwPfLgZByWZi5m3READjJSur; _gid=GA1.2.1388636281.1655395233; stripchat_com_sessionId=9e379ccdab10ddee5e93e5d7d65fae9f3b30b2583f0fb997e094099452d0; stripchat_com_sessionRemember=1; userWatchHistoryIds=30042591; _gat=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        
        'from': ''+año+'-'+mes+'-'+dia+'T05:00:00Z',
        'until': año2+'-'+mes2+'-'+dia2+'T04:59:59Z',
        'uniq': 'mf193dw8tqgvoj76',
    }
    
    response = requests.get('https://es.stripchat.com/api/front/users/73672961/earnings?from='+año+'-'+mes+'-'+dia+'T05%3A00%3A00Z&until='+año2+'-'+mes2+'-'+dia2+'T04%3A59%3A59Z&uniq=mf193dw8tqgvoj76', headers=headers, cookies=cookies)
    

    eq = json.loads(response.text)
    print(eq)

    for i in range (0, len(eq['earnings'])):
        db.child('stripchat').child(eq['earnings'][i]['username']).child(año+mes+str(quincena)).child(dia).set(eq['earnings'][i]['total']/20)
    
