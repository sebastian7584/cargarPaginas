
import pathlib
from os import remove
from typing import Type
import pandas
import numpy as np
import pyrebase 
import webbrowser


def cargarDatosFlirt4free(dia,mes,año,db):

    print('Estadisticas Flirt4Free')
    quincena=""

    if int(dia) >15:
        quincena=2
    if int(dia) <16:
        quincena=1   





    ejemplo_dir= "archivos"
    direct=[]
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        direct.append(fichero.name)


    filename = ejemplo_dir + "\\"+direct[0]

    data = pandas.read_csv(filename)
    data1 = np.asarray(data)
    cantidad = data1.shape[0]
    remove(filename)

    for i in range (0, cantidad ) :
        db.child('flirt4free').child(str(data1[i][0])).child(año+mes+str(quincena)).child(dia).set(data1[i][21]*1.86/60)

    
    #for i in range (0,cantidad-1):
        #db.child('flirt4free').child(data[i][0]).child(año+mes+str(quincena)).child(dia).set(data[i][20])





