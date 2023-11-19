from paginas.cam4 import cargarDatosCam4
from data.firebaseConfig import db

for i in range (1,15):
    print(i)
    año ='2022'
    mes='03'
    if i < 10 :
        dia='0'+str(i)
    else : dia = i

    dia = str(dia)
    cargarDatosCam4(dia,mes,año,db)