from calendar import month
from selenium import webdriver
import time
from datetime import date
from paginas.stripchat2 import cargarDatosStripchat2

from paginas.chaturbate import cargarDatosChaturbate
from paginas.chaturbate2 import cargarDatosChaturbate2
from paginas.chaturbate3 import cargarDatosChaturbate3
from paginas.stripchat import cargarDatosStripchat
from paginas.cam4 import cargarDatosCam4
from paginas.flirt4free import cargarDatosFlirt4free
from paginas.streamate import cargarDatosStreamate

from paginas.bongaApi import datosBonga
from paginas.bongaListaModelos import modelos



from data.firebaseConfig import db
from data.dia import diaActual,diaSiguiente,hora, diaDespuesDe

from selenium.webdriver.chrome.options import Options as ChromeOptions



def cargarDiaEstadisticas(idia,imes,iaño):
    for i in range (idia,idia+1): 
        print(i)
        año=iaño
        mes=imes
        if i < 10 :
            dia='0'+str(i)
        else : dia = i
        dia = str(dia)
        dd,md,ad = diaDespuesDe(dia,mes,año)
        dia = str(dia)
        if int(dia) >15:
            quincena=2
            
        if int(dia) <16:
            quincena=1   

        cargarDatosChaturbate(dia,mes,año,db)
        cargarDatosChaturbate2(dia,mes,año,db)
        cargarDatosChaturbate3(dia,mes,año,db)
        cargarDatosStripchat(dia,mes,año,dd,md,ad,db)
        cargarDatosStripchat2(dia,mes,año,dd,md,ad,db)




        options = ChromeOptions()

        driver = webdriver.Chrome(chrome_options=options)
        driver.get('https://www.cam4.es/studio/login')

        time.sleep(2)

        user= driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_usernameInput"]')

        if user is not None:
            user.send_keys("olimpostudio")
        password = driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_passwordInput"]')
        if password is not None:
            password.send_keys("Zeus2020*")
        time.sleep(2)

        sumbit = driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_submitButton"]/span')
        if sumbit is not None:
            sumbit.click()
        time.sleep(2)
        temcookies = driver.get_cookies()


        driver.quit()
        cookiesC=''


        for i in range (0,len(temcookies)):
            if temcookies[i]['name'] == 'JSESSIONID':
                cookiesC=temcookies[i]['value']
        print(cookiesC)
        cargarDatosCam4(dia,mes,año,db,cookiesC)

        for x in modelos:
            data= datosBonga(año,mes,dia,x)
            if data is not None:
                model=(data['username'])
                print(model)
                valor=(data['with_percentage_rate_income'])
                valor =float(f"{valor:.2f}")
                if valor > 0:
                    db.child('bonga').child(model).child(año+mes+str(quincena)).child(dia).set(valor)
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\usuario\\Documents\\olimpo\\cargar_paginas\\archivos",
        "download.Prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True})
        browser = webdriver.Chrome(chrome_options=options) 
        estadistica= 'https://studios.flirt4free.com/broadcasters/stats-export.php?a=studio_overview&studio=GHJQ&date_start='+año+'-'+mes+'-'+dia+'&date_end='+año+'-'+mes+'-'+dia+'&format=csv'
        browser.get(estadistica)
        user = browser.find_element_by_id('username_field')
        if user is not None:
            user.send_keys("olimpostudio")
        password = browser.find_element_by_id('password_field')
        if password is not None:
            password.send_keys("Zeus2020**")
        time.sleep(2)
        agree = browser.find_element_by_name('checkbox_agreement')
        if agree is not None:
            agree.click()
        sumbit = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/form/button')
        if sumbit is not None:
            sumbit.click()

        time.sleep(4)
        browser.quit()
        print(dia)
        cargarDatosFlirt4free(dia,mes,año,db)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\usuario\\Documents\\olimpo\\cargar_paginas\\archivos",
        "download.Prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True})
        browser = webdriver.Chrome(chrome_options=options) 
        estadistica= 'https://modelcenter.livejasmin.com/es/payout/income-statistics?fromDate='+año+'-'+mes+'-'+dia+'&toDate='+año+'-'+mes+'-'+dia+'&status=all&category=all'
        browser.get(estadistica)
        user = browser.find_element_by_id('emailOrNick')
        if user is not None:
            user.send_keys("olimpowebstudio@gmail.com")
        password = browser.find_element_by_id('password')
        if password is not None:
            password.send_keys("Zeus2020**")
        time.sleep(2)
        sumbit = browser.find_element_by_xpath('/html/body/div[3]/div[2]/ph-row/ph-col/div/div/form/div/div[3]/button')
        if sumbit is not None:
            sumbit.click()
        time.sleep(4)
        browser.get(estadistica)

        for h in range (2,100):
            dato1= browser.find_element_by_xpath("/html/body/div[5]/div[2]/section/div[1]/div[3]/table/tbody/tr["+str(h)+"]/td[1]")
            dato2= browser.find_element_by_xpath("/html/body/div[5]/div[2]/section/div[1]/div[3]/table/tbody/tr["+str(h)+"]/td[2]")
            print(dato1.text, dato2.text)
            if dato1.text == 'Income Summary:':
                break
            
            if int(dia) >15:
                quincena=2
            if int(dia) <16:
                quincena=1   
            db.child('jasmin').child((dato1.text)).child(año+mes+str(quincena)).child(dia).set(str(dato2.text[1:len(dato2.text)]))
            


        time.sleep(4)
        browser.quit()

        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\usuario\\Documents\\olimpo\\cargar_paginas\\archivos",
        "download.Prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True})
        browser = webdriver.Chrome(chrome_options=options) 
        browser.get('https://www.streamatemodels.com/smm/login.php')
        user = browser.find_element_by_id('login-form-username')
        if user is not None:
            user.send_keys("olimpowebstudio@gmail.com")
        password = browser.find_element_by_id('login-form-password')
        if password is not None:
            password.send_keys("Zeus2020**")
        browser.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        
        sumbit = browser.find_element_by_xpath('//*[@id="login-form-submit"]')
        if sumbit is not None:
            sumbit.click()


        print('Estadisticas Streamate')
        mesfecha=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] 


        estadistica= 'https://www.streamatemodels.com/smm/reports/earnings/EarningsReportPivot.php?range=day&earnday='+mesfecha[int(mes)-1]+'%20'+dia+',%20'+año+'&earnyear=2021&earnweek=1626480000&studio_filter=0&format=csv_summary'
        browser.get(estadistica)
        time.sleep(2)
        browser.quit()
        print(dia)
        cargarDatosStreamate(dia,mes,año,db)

now= date.today()
idia= now.day
imes= now.month
if imes < 10 :
    imes='0'+str(imes)
else : imes = imes
imes = str(imes)

if idia >1:
    idia=idia-1
    cargarDiaEstadisticas(idia,imes,str(now.year))