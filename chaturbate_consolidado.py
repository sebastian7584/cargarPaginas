from paginas.chaturbate import cargarDatosChaturbate
from paginas.chaturbate2 import cargarDatosChaturbate2
from data.dia import diaAnterior
from data.firebaseConfig import db

d,m,a = diaAnterior()

cargarDatosChaturbate(d,m,a,db)
cargarDatosChaturbate2(d,m,a,db)
