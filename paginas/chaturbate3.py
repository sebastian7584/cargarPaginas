import requests  #Importamos la librería requests
from datetime import date

def cargarDatosChaturbate3(dia,mes,año,db):
    today = date.today()
    print('Estadisticas chaturbate')
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    

    URL = 'https://es.chaturbate.com/affiliates/apistats/?username=rossitokens&token=dlCTwFZ8CYrcWVJiUcAY7rWV&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0&date_day='+dia+'&date_month='+mes+'&date_year='+año+'&start_date_day=1&start_date_month=7&start_date_year=2021&end_date_day=15&end_date_month=7&end_date_year=2021' #configuramos la url
    #solicitamos la información y guardamos la respuesta en data.
    if dia != str(today.day):
        data = requests.get(URL) 

        data = data.json() #convertimos la respuesta en dict
        if data['stats'] == []: 
            print('dia sin estadisticas ch3')
        else: 
            
            for i in range (0,len(data['stats'][0]['rows'])):
                db.child('chaturbate').child(data['stats'][0]['rows'][i][0]).child(año+mes+str(quincena)).child(dia).set(data['stats'][0]['rows'][i][2])

    else: print('Solo se puede hasta dia anterior al actual')

