from data.dia import diaActual,diaSiguiente,hora, diaDespuesDe
from paginas.stripchat import cargarDatosStripchat
from paginas.stripchat2 import cargarDatosStripchat2
from paginas.stripchat3 import cargarDatosStripchat3
from data.firebaseConfig import db
import time


for i in range (16,31):
    a = '2023'
    m= '06'
    if i < 10 :
        d='0'+str(i)
    else : d = i
    d = str(d)
    d2,m2,a2 = diaDespuesDe(d,m,a)
    print(d)
    cargarDatosStripchat(d,m,a,d2,m2,a2,db)
    cargarDatosStripchat2(d,m,a,d2,m2,a2,db)
    cargarDatosStripchat3(d,m,a,d2,m2,a2,db)
  