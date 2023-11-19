from data.dia import diaActual,diaSiguiente,hora, diaDespuesDe,diaAnterior
from paginas.stripchat import cargarDatosStripchat
from data.firebaseConfig import db

hr =hora()
if True:
    if int(hr) <2 :
        d,m,a = diaAnterior()
        d2,m2,a2 = diaDespuesDe(d,m,a)
        
    else:
        d,m,a = diaActual()
        d2,m2,a2 = diaSiguiente()
if int(d) >= 1:
    cargarDatosStripchat(d,m,a,d2,m2,a2,db)

