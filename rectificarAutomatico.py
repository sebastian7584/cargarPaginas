from data.firebaseConfig import db
from datetime import date
import requests

año='2022'
mes='02'
quincena='1'
fecha= '15'

def modelosCargar(pagina,año,mes,quincena,fecha):
    today = date.today()
    

    modelos2 = db.child(pagina).get()
    if modelos2 is not None:
        valorPagina=0
        for modelos2 in modelos2.each():
            usuario = modelos2.key()
            valores = db.child(pagina).child(usuario).child(año+mes+str(quincena)).get()
            valorPaginaModelo=0
            if valores.val() is not None:
                for valores in valores.each():
                    if valores.val() is not None:
                        if str(valores.key()) <= fecha:
                            #print(pagina+usuario)
                            valorPaginaModelo = valorPaginaModelo + float(valores.val())
            valorPagina = valorPagina + valorPaginaModelo
    print('sistema ',pagina, valorPagina)
    return valorPagina

chatur = modelosCargar('chaturbate',año,mes,quincena,fecha)
cam4 = modelosCargar('cam4',año,mes,quincena,fecha)
stream = modelosCargar('streamate',año,mes,quincena,fecha)
strip = modelosCargar('stripchat',año,mes,quincena,fecha)
f4f = modelosCargar('flirt4free',año,mes,quincena,fecha)
jasmin = modelosCargar('jasmin',año,mes,quincena,fecha)
bonga = modelosCargar('bonga',año,mes,quincena,fecha)
skyprivate = modelosCargar('skyprivate',año,mes,quincena,fecha)
imlive = modelosCargar('imlive',año,mes,quincena,fecha)


totalPa=chatur+cam4+stream+f4f+jasmin

print(totalPa)