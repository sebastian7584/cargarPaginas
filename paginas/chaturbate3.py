import requests  #Importamos la librería requests
from datetime import date

def cargarDatosChaturbate3(dia,mes,año,db):
    today = date.today()
    print('Estadisticas chaturbate')
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1    

    URL = 'https://es.chaturbate.com/affiliates/apistats/?username=rossitokens&token=dlCTwFZ8CYrcWVJiUcAY7rWV&stats_breakdown=sub_account__username&campaign=&search_criteria=2&period=0'+f'&date={año}-{mes}-{dia}' #configuramos la url
    #solicitamos la información y guardamos la respuesta en data.
    if dia != str(today.day):
        data = requests.get(URL) 

        data = data.json() #convertimos la respuesta en dict
        if data['stats'] == []: 
            print('dia sin estadisticas ch3')
        else:
            if  len(data['stats'])>1:
                data = data['stats'][3]
            else: 
                data = data['stats'][0] 
            
            for i in range (0,len(data['rows'])):
                db.child('chaturbate').child(data['rows'][i][0]).child(año+mes+str(quincena)).child(dia).set(data['rows'][i][2])

    else: print('Solo se puede hasta dia anterior al actual')

