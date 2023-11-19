from datetime import date, datetime

fechas = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
fecha= date.today()
año = str(fecha.year)
mes = str(fecha.month)
dia = str(fecha.day)
if int(mes) < 10 :
        mes='0'+mes

def diaAnterior():
    año2= año
    if dia == '01':
        mes2= str(int(mes)-1)
        if int(mes2) < 10 :
            mes2='0'+mes2
        if mes == '01':
            mes2 = '12'
            año2 = str(int(año)-1)
        dia2=fechas[mes2]  
    else:
        dia2=str(int(dia)-1)
        mes2=str(int(mes))
    if int(dia2) < 10 :
        dia2 ='0'+dia2
    if int(mes2) < 10 :
            mes2='0'+mes2
    return dia2, mes2, año2

def diaActual():
    d= dia
    m= mes
    a=año
    if int(d) < 10 :
        d ='0'+d
    return d,m,a

def diaSiguiente():
    if dia == str(fechas[mes]):
        if mes== '12':
            mes2= '1'
            año2= str(int(año)+1)
        else:            
            mes2= str(int(mes)+1)
            año2 = año
        dia2='1'
    else:
        dia2=str(int(dia)+1)
        mes2=str(int(mes))
        año2 = año

    if int(dia2) < 10 :
        dia2 ='0'+dia2

    if int(mes2) < 10 :
        mes2='0'+str(int(mes2))
    return dia2,mes2,año2

def hora():
    hr = datetime.now().hour
    return hr

def finDia():
    resultado = False
    hr= hora()
    if int(hr) < 10:
        hr = '0'+ str(int(hr))
    if hr == '01' or hr == '02':
        resultado=True
    return resultado 

def diaDespuesDe(dia1,mes1,año1):
    if dia1 == str(fechas[mes1]):
        if mes1== '12':
            mes2= '1'
            año2= str(int(año1)+1)
        else:            
            mes2= str(int(mes)+1)
            año2 = año
        dia2='1'
    else:
        dia2=str(int(dia1)+1)
        mes2=str(int(mes1))
        año2 = año1

    if int(dia2) < 10 :
        dia2 ='0'+dia2

    if int(mes2) < 10 :
        mes2='0'+mes2
    print(dia2, mes2, año2)
    return dia2,mes2,año2