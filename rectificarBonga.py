from data.dia import diaActual
from paginas.bongaApi import datosBonga
from paginas.bongaListaModelos import modelos
from data.firebaseConfig import db


for i in range (1,16):
    print(i)
    año ='2023'
    mes='09'
    if i < 10 :
        dia='0'+str(i)
    else : dia = i

    dia = str(dia)
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1   
    
    for i in modelos:
        print(i)
        data= datosBonga(año,mes,dia,i)
        if data is not None:
            model=(data['username'])
            valor=(data['with_percentage_rate_income'])
            valor =float(f"{valor:.2f}")
            if valor > 0:
                db.child('bonga').child(model).child(año+mes+str(quincena)).child(dia).set(valor)



