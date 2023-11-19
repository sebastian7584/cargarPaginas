import json
import requests


def cargarDatosCam4(dia,mes,año,db,cookiesC):

    print('Estadisticas cam4')

    
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    




    cookies = {
        'JSESSIONID': cookiesC,
        
       
        
        
    }
 



    params = (
        ('from', año+'-'+mes+'-'+dia),
        ('to', año+'-'+mes+'-'+dia),
    )
    data = '{username:olimpostudio,password:Zeus2020*}'
    

    response = requests.get('https://www.cam4.es/rest/v1.0/reporting/studio/olimpostudio/broker-insights-by-user?from='+año+'-'+mes+'-'+dia+'&to='+año+'-'+mes+'-'+dia, cookies=cookies, data=data)



    ep= json.loads(response.text)
    print(ep)

    for i in range (0, len(ep)):
        db.child('cam4').child(ep[i]['performerName']).child(año+mes+str(quincena)).child(dia).set(ep[i]['amount']/10)
        




