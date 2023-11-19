from data.dia import diaActual
from paginas.bongaApi import datosBonga
from paginas.bongaListaModelos import modelos
from data.firebaseConfig import db


d,m,a = diaActual()
print(len(modelos))

for i in modelos:
    data= datosBonga(a,m,d,i)
    if data is not None:
        print(data['username'])
        print(data['with_percentage_rate_income'])

