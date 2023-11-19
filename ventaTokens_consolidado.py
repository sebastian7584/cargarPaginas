
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pyrebase

linkChatur= 'https://es.chaturbate.com/statsapi/?username=olimpostudio&token=H7tzkuPi7FXZgw8LAzuVGdwh'
data = requests.get(linkChatur)
data=data.json()
totalTokens= data['token_balance']

if totalTokens >0:
    firebaseConfig= {
        'apiKey': "AIzaSyDIVfFFVPeS-IItgh2ExPr2JPLCjh7gufI",
        'authDomain': "groovy-bonus-310519.firebaseapp.com",
        'databaseURL': "https://groovy-bonus-310519-default-rtdb.firebaseio.com",
        'projectId': "groovy-bonus-310519",
        'storageBucket': "groovy-bonus-310519.appspot.com",
        'messagingSenderId': "509390918244",
        'appId': "1:509390918244:web:84a5624f3ef04d23d20571",
        'measurementId': "G-DYE6S50CY9"
        }

    firebase=pyrebase.initialize_app(firebaseConfig)

    db=firebase.database()


    options = ChromeOptions()
    options.add_argument('--profile-directory=Profile 3')
    options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://es.chaturbate.com/p/olimpostudio/?tab=tokens')

    login = driver.find_element_by_link_text("LOG IN")
    time.sleep(3)
    if login is not None:
        login.click()
    time.sleep(1)
    user = driver.find_element_by_id("username")
    if user is not None:
        user.send_keys("olimpostudio")
    time.sleep(1)
    password = driver.find_element_by_id("password")
    if password is not None:
        password.send_keys("Zeus2020**")
    time.sleep(1)
    loginBoton = driver.find_element_by_id("id_login_btn")
    if loginBoton is not None:
        loginBoton.click()
    time.sleep(1)

    lista = []
    confirmacion = True
    fechas= ['ini','ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
    ultimoDato = db.child('ventaTokens').child('chaturbate').child('ultimoDato').get()


    for i in range (2, 32):
        dato= driver.find_element_by_xpath("//*[@id='roomTabs']/div[6]/div[3]/div/table/tbody/tr["+str(i)+"]/td[2]")
        dato2= driver.find_element_by_xpath("//*[@id='roomTabs']/div[6]/div[3]/div/table/tbody/tr["+str(i)+"]/td[3]")
        dato3= driver.find_element_by_xpath("//*[@id='roomTabs']/div[6]/div[3]/div/table/tbody/tr["+str(i)+"]/td[4]")
        dato4= driver.find_element_by_xpath("//*[@id='roomTabs']/div[6]/div[3]/div/table/tbody/tr["+str(i)+"]/td[1]")
        if dato is not None:
            if dato2 is not None:

                lista.append([dato.text,dato2.text,dato3.text,dato4.text])

    posicion=0
    for i in range(0,len(lista)):
        if lista[i][0][0:3] == 'Tip':
            claveUltimoDia = str(lista[i][3][0:2])
            if int(claveUltimoDia) < 10:a=1
            else : a=0
            claveUltimoMes = str(fechas.index(lista[i][3][6-a:9-a]))
            claveUltimoAño = '2021'
            sumHora=0
            if int(lista[i][3][20-a:26-a].index(':')) ==2:
                sumHora=1
            claveUltimoHora= lista[i][3][20-a:26+sumHora-a]
            if int(claveUltimoDia) <10: claveUltimoDia = '0'+claveUltimoDia
            if int(claveUltimoMes) <10: claveUltimoMes= '0'+claveUltimoMes 
            claveUltimo= claveUltimoAño+claveUltimoMes+claveUltimoDia+claveUltimoHora
            ini = lista[i][0].index('(')
            fin = lista[i][0].index(')')
            lista[i][0] = lista[i][0][ini+1:fin]
            if lista[i][0]+'-'+lista[i][1]+'-'+lista[i][2]+'-'+claveUltimo == ultimoDato.val():
                posicion = i
                print('posicion establecida en '+str(posicion))


    if posicion ==0: totalTokensPagina=0
    else:
        totalTokensPagina=0
        for i in range (0,posicion):
            if lista [i][0][0:3] != 'Tra':
                totalTokensPagina = totalTokensPagina + int(lista[i][1])
    if totalTokens == totalTokensPagina:
        print('valores iguales')
        tokensToCash = driver.find_element_by_xpath('//*[@id="roomTabs"]/div[6]/div[2]/a')
        if tokensToCash is not None:
            tokensToCash.click()
        inputTokensToCash = driver.find_element_by_xpath('//*[@id="id_amount"]')
        if inputTokensToCash is not None:
            inputTokensToCash.clear()
            inputTokensToCash.send_keys(str(totalTokensPagina))
        botonTokensToCash = driver.find_element_by_xpath('//*[@id="cashout_form"]/input[3]')
        if botonTokensToCash is not None:
            botonTokensToCash.click()
        if int(totalTokensPagina)!= 0:
            confirm= driver.switch_to_alert()
            confirm.accept()
        time.sleep(2)
        for i in range (0,posicion):
            if lista[i][0][0:3] != 'Tra':
                claveDia = str(lista[i][3][0:2])
                if int(claveDia) < 10:a=1
                else : a=0
                claveMes = str(fechas.index(lista[i][3][6-a:9-a]))
                claveAño = '2021'
                if int(claveDia) >15: claveQuincena=2
                if int(claveDia) <16: claveQuincena=1 
                if int(claveDia) <10: claveDia = '0'+claveDia
                if int(claveMes) <10: claveMes= '0'+claveMes
                sumHora=0
                if int(lista[i][3][20-a:26-a].index(':')) ==2:
                    sumHora=1
                db.child('ventaTokens').child('chaturbate').child('modelos').child(lista[i][0]).child(claveAño+claveMes+str(claveQuincena)).child(claveAño+'-'+claveMes+'-'+claveDia+'-'+lista[i][3][20-a:26+sumHora-a]+lista[i][2]).set(lista[i][1])
                if confirmacion == True:
                    print('registrado nuevo ultimo Dato')
                    db.child('ventaTokens').child('chaturbate').child('ultimoDato').set(lista[i][0]+'-'+lista[i][1]+'-'+lista[i][2]+'-'+claveAño+claveMes+claveDia+lista[i][3][20-a:26+sumHora-a])
                    confirmacion= False

driver.quit()
