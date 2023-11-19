import pathlib
from os import remove
import time
import pandas
import numpy as np

def cargarDatosStreamate(dia,mes,año,db):
    if int(dia) >15:
        quincena=2
    if int(dia) <16:
        quincena=1  
    time.sleep(2)
    ejemplo_dir= "C:\\Users\\usuario\\Documents\\olimpo\\cargar_paginas\\archivos"
    direct=[]
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        direct.append(fichero.name)

    nombre=[]
    monto=[]
    junta=[]

    alica=ejemplo_dir + '\\'+ direct[0]
    print(alica)

    filename = ejemplo_dir + "\\"+direct[0]

    data = pandas.read_csv(filename, encoding='latin-1')
    data1 = np.asarray(data)
    cantidad = data1.shape[0]

    for i in range (0,cantidad):
        if data1[i][0]>0:
            nombre.append(data1[i][1])
            monto.append(data1[i][7][1:len(data1[i][7])])




    for i in range (0,len(nombre)):
        db.child('streamate').child(nombre[i]).child(año+mes+str(quincena)).child(dia).set(monto[i])

    remove(alica)

#cargarDatosStreamate('29','08','2023')

