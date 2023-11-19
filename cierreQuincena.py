from data.firebaseConfig import db
import locale
from datetime import date

año='2023'
año2='2023'
mes='11'
mes2='11'
dia='15'
quincena2=2
dolar=3800


def saldoGeneral(año,mes,dia,dolar):

    today = date.today()
    # if today.month <10:
    #     mes= '0'+str(today.month)
    # else:
    #     mes = str(today.month)
    # dia = str(today.day)
    if int(dia) >15:
        quincena=2
    if int(dia) <16:
        quincena=1 

    
    totalDolares=0
    totalPesos=0
    totalAdel = 0
    totalDis = 0
    totalGan=0
    i=1
    locale.setlocale( locale.LC_ALL, '' )
    modelos = db.child('modelos').get()
    for modelos in modelos.each():
        codigo=modelos.key()
        porcentaje=modelos.val()['porcentaje']
        paginas=db.child('modelos').child(codigo).child('paginas').get()
        dolares = 0
        totalAdelantado=0
        modelo= modelos.val()['nombre']
        saldoInicial=db.child('modelos').child(codigo).child('cierreQuincena').child(año+mes+str(quincena)).child('saldoAnterior').get()
        saldoInicial = saldoInicial.val()
        if saldoInicial is None: saldoInicial=0
        if paginas.val() != None:
            for paginas in paginas.each():
                valores = db.child(paginas.val()['pagina']).child(paginas.val()['modelo']).child(año+mes+str(quincena)).get()
                sumt=0
                if valores.val() != None:
                    for valores in valores.each():
                        if valores.val() is not None:
                            sumt=sumt+ float(valores.val())
                    dolares = dolares + sumt
                adelantos = db.child('modelos').child(codigo).child('adelantos').child(año+mes+str(quincena)).get()
                adelantado= 0
            if adelantos.val() != None :
                for adelantos in adelantos.each():
                    adelantado = adelantado + float(adelantos.val()['valor'])
                totalAdelantado = totalAdelantado + adelantado
        pesos= int(dolares * int(porcentaje)/100 * int(dolar))
        gan= int(dolares*(100-int(porcentaje))/100*int(dolar))
        disponible = pesos - totalAdelantado - saldoInicial          
        locale.currency( pesos )
        locale.currency( totalAdelantado )
        locale.currency( disponible )
        totalDolares= totalDolares + dolares
        totalPesos = totalPesos + pesos
        totalAdel = totalAdel + totalAdelantado
        totalDis = totalDis + disponible
        totalGan = totalGan + gan
        locale.currency( totalDolares )
        locale.currency( totalPesos )
        locale.currency( totalAdel )
        locale.currency( totalDis )
        locale.currency( totalGan )
        locale.currency( saldoInicial)
        print(codigo,modelo,porcentaje,dolares,pesos,totalAdelantado,disponible)
        db.child('modelos').child(codigo).child('cierreQuincena').child(año+mes+str(quincena)).child('cierre').set(disponible)
        db.child('modelos').child(codigo).child('cierreQuincena').child(año2+mes2+str(quincena2)).child('saldoAnterior').set(-disponible)


saldoGeneral(año,mes,dia,dolar)
        