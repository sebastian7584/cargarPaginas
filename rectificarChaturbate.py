from paginas.chaturbate import cargarDatosChaturbate
from paginas.chaturbate2 import cargarDatosChaturbate2
from paginas.chaturbate3 import cargarDatosChaturbate3
from data.firebaseConfig import db

for i in range (31,32):
    print(i)
    año='2023'
    mes='10'
    if i < 10 :
        dia='0'+str(i)
    else : dia = i
    dia = str(dia)
    cargarDatosChaturbate(dia,mes,año,db)
    cargarDatosChaturbate2(dia,mes,año,db)
    # cargarDatosChaturbate3(dia,mes,año,db)