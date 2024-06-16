from selenium import webdriver
# import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time

from paginas.stripchat2 import cargarDatosStripchat2
from paginas.stripchat3 import cargarDatosStripchat3

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
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests



class Scraping:

    def __init__(self,html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.html = html

    def extrarDataTablas(self):
        tabla = self.soup.find('tbody')

        if tabla:
            filas = tabla.find_all('tr')
            datos_tabla = []
            for fila in filas:
                celdas = fila.find_all('td')
                datos_fila=[]
                for celda in celdas:
                    datos_fila.append(celda.get_text())
                datos_tabla.append(datos_fila)
        return datos_tabla



#chromedriver_autoinstaller.install()

for i in range(15,16):
    print(i)
    año='2024'              
    mes='06'      
    if i < 10 :
        dia='0'+str(i)
    else : dia = i
    dia = str(dia)
    fecha_actual = datetime(int(año), int(mes), int(dia))
    nueva_fecha = fecha_actual + timedelta(days=1)
    dd = str(nueva_fecha.day)
    md = str(nueva_fecha.month)
    ad = str(nueva_fecha.year)
    if int(md) <10:
        md = f'0{int(md)}'
    print(f'{año}-{mes}-{dia} a {ad}-{md}-{dd}')
    if int(dd) < 10 :
        dd ='0'+str(dd)
    # dd,md,ad = diaDespuesDe(dia,mes,año)
    dia = str(dia)
    if int(dia) >15:
        quincena=2
        
    if int(dia) <16:
        quincena=1   
    
    

    # cargarDatosChaturbate(dia,mes,año,db)
    # cargarDatosChaturbate2(dia,mes,año,db)
    # cargarDatosChaturbate3(dia,mes,año,db)
    cargarDatosStripchat(dia,mes,año,dd,md,ad,db)
    cargarDatosStripchat2(dia,mes,año,dd,md,ad,db)
    # cargarDatosStripchat3(dia,mes,año,dd,md,ad,db)




    # options = ChromeOptions()

    # driver = webdriver.Chrome(chrome_options=options)
    # driver.get('https://www.cam4.es/studio/login')

    # time.sleep(8)

    # user= driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_usernameInput"]')

    # if user is not None:
    #     user.send_keys("olimpostudio")
    # password = driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_passwordInput"]')
    # if password is not None:
    #     password.send_keys("Zeus2020*")
    # time.sleep(2)

    # sumbit = driver.find_element_by_xpath('//*[@id="tUZ2be9k_loginFrom_submitButton"]/span')
    # if sumbit is not None:
    #     sumbit.click()
    # time.sleep(2)
    # temcookies = driver.get_cookies()


    # driver.quit()
    # cookiesC=''


    # for i in range (0,len(temcookies)):
    #     if temcookies[i]['name'] == 'JSESSIONID':
    #         cookiesC=temcookies[i]['value']
    # print(cookiesC)
    # cargarDatosCam4(dia,mes,año,db,cookiesC)
        
    # BONGA

    # for x in modelos:
    #     data= datosBonga(año,mes,dia,x)
    #     if data is not None:
    #         model=(data['username'])
    #         print(model)
    #         valor=(data['with_percentage_rate_income'])
    #         valor =float(f"{valor:.2f}")
    #         if valor > 0:
    #             db.child('bonga').child(model).child(año+mes+str(quincena)).child(dia).set(valor)
    

    # ruta_descargas = "archivos"
    # ruta_perfil = r"C:\Users\SebastianMoncada\AppData\Local\Google\Chrome\\User Data\Profile 4"
    # opciones = Options()
    # opciones.add_argument("--user-data-dir=" + ruta_perfil)
    # s = Service('chromedriver.exe')
    # browser = webdriver.Chrome(service=s ,options=opciones)
    # estadistica= 'https://studios.flirt4free.com/broadcasters/stats-export.php?a=studio_overview&studio=GHJQ&date_start='+año+'-'+mes+'-'+dia+'&date_end='+año+'-'+mes+'-'+dia+'&format=csv'
    # browser.get(estadistica)
    # user = browser.find_element('id', 'username_field')
    # if user is not None:
    #     user.send_keys("olimpostudio")
    # password = browser.find_element('id', 'password_field')
    # if password is not None:
    #     password.send_keys("Zeus2020**")
    # time.sleep(2)
    # agree = browser.find_element('name', 'checkbox_agreement')
    # if agree is not None:
    #     agree.click()
    # sumbit = browser.find_element('xpath', '/html/body/div[1]/div/div/div[2]/div/div[2]/form/button')
    # if sumbit is not None:
    #     sumbit.click()

    # time.sleep(3)
    # browser.quit()
    # print(dia)
    # cargarDatosFlirt4free(dia,mes,año,db)


    #JASMIN

    # options = Options()
    # # options.add_argument("--headless=new")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # # options.add_experimental_option("prefs", {
    # #     "download.default_directory": "/var/adminstudioolimpo/backend/archivos",
    # #     "download.prompt_for_download": False,
    # #     "download.directory_upgrade": True,
    # #     "safebrowsing_for_trusted_sources_enabled": False,
    # #     "safebrowsing.enabled": False
    # # })
    # browser = webdriver.Chrome(options=options)
    # pagina = 'https://modelcenter.livejasmin.com/es/login'
    # estadistica= 'https://modelcenter.livejasmin.com/es/payout/income-statistics?fromDate='+año+'-'+mes+'-'+dia+'&toDate='+año+'-'+mes+'-'+dia+'&status=all&category=all'
    # browser.get(pagina)
    # user = browser.find_element('id', 'emailOrNick')
    # if user is not None:
    #     user.send_keys("olimpowebstudio@gmail.com")
    # password = browser.find_element('id', 'password')
    # if password is not None:
    #     password.send_keys("Zeus2020**")
    # time.sleep(2)
    # # sumbit = browser.find_element(By.CSS_SELECTOR, "div > button[type='submit']")
    # sumbit = browser.find_element('xpath', "/html/body/div[5]/div[2]/ph-row/ph-col/div/div/form/div/div[3]/button")
    # if sumbit is not None:
    #     sumbit.click()
    # time.sleep(4)
    # browser.get(estadistica)
    # sopa = browser.page_source

    # sup = Scraping(sopa)
    # data = sup.extrarDataTablas()
    # for i in data:
    #     if 'Modelo' in i[0]:
    #         continue
    #     if 'Income Summary' in i[0]:
    #         break
    #     modelo = i[0].replace('\n','').replace('\t','')
    #     cantidad = i[1].replace('$','')
    #     print(modelo, cantidad)
    #     db.child('jasmin').child((modelo)).child(año+mes+str(quincena)).child(dia).set(str(cantidad))

    # for h in range (2,100):
    #     try:
    #         dato1= browser.find_element_by_xpath("/html/body/div[5]/div[2]/section/div[1]/div[3]/table/tbody/tr["+str(h)+"]/td[1]")
    #         dato2= browser.find_element_by_xpath("/html/body/div[5]/div[2]/section/div[1]/div[3]/table/tbody/tr["+str(h)+"]/td[2]")
    #         print(dato1.text, dato2.text)
    #         if dato1.text == 'Income Summary:':
    #             break
            
    #         if int(dia) >15:
    #             quincena=2
    #         if int(dia) <16:
    #             quincena=1   
    #         db.child('jasmin').child((dato1.text)).child(año+mes+str(quincena)).child(dia).set(str(dato2.text[1:len(dato2.text)]))
    #     except Exception: break    


    # time.sleep(4)
    # browser.quit()

    # #STREAMATE

    # options = Options()
    
    
    # options.add_experimental_option("prefs", {
    #     "download.default_directory": f"archivos",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing_for_trusted_sources_enabled": False,
    #     "safebrowsing.enabled": False
    # })
    # browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # time.sleep(7)
    # user = browser.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div/form/fieldset/span[1]/div/input')
    # if user is not None:
    #     user.send_keys("olimpowebstudio@gmail.com")
    # password = browser.find_element_by_id('password')
    # if password is not None:
    #     password.send_keys("Zeus2020**")
    # browser.execute_script("window.scrollTo(0, 300)")
    # time.sleep(2)
    
    # sumbit = browser.find_element_by_xpath('/html/body/div/div/div/main/div/div/div/div/form/fieldset/button')
    # if sumbit is not None:
    #     sumbit.click()


    # print('Estadisticas Streamate')
    # mesfecha=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] 

    # time.sleep(3)
    # estadistica= 'https://www.streamatemodels.com/smm/reports/earnings/EarningsReportPivot.php?range=day&earnday='+mesfecha[int(mes)-1]+'%20'+dia+',%20'+año+'&earnyear=2021&earnweek=1626480000&studio_filter=0&format=csv_summary'
    # browser.get(estadistica)
    # time.sleep(2)
    # browser.quit()
    # print(dia)
    # cargarDatosStreamate(dia,mes,año,db)


    # IMLIVE

    # options = Options()
    # # options.add_argument("--headless=new")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_experimental_option("prefs", {
    #     "download.default_directory": "/var/adminstudioolimpo/backend/archivos",
    #     "download.prompt_for_download": False,
    #     "download.directory_upgrade": True,
    #     "safebrowsing_for_trusted_sources_enabled": False,
    #     "safebrowsing.enabled": False
    # })
    # browser = webdriver.Chrome(options=options)
    # pagina = 'https://studio.imlive.com/#/'
    # estadistica= 'https://studio.imlive.com/#/Studio/Statistics/HostReport'
    # browser.get(pagina)
    # log = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/a/span')
    # if log is not None:
    #     log.click()
    # user = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[2]/input')
    # if user is not None:
    #     user.send_keys("olimpostudioll")
    # password = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[3]/input')
    # if password is not None:
    #     password.send_keys("Zeus2020**")
    # time.sleep(2)
    # sumbit = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[4]')
    # if sumbit is not None:
    #     sumbit.click()
    # time.sleep(4)
    # browser.get(estadistica)
    # time.sleep(4)
    # browser.get(estadistica)
    # # sumbit = browser.find_element('xpath', '/html/body/div/div/div[1]/div[2]/div/section/div[2]/div[2]/div/div/div[2]')
    # # if sumbit is not None:
    # #     sumbit.click()
    # time.sleep(4)
    # sopa = browser.page_source
    # print(sopa)
    # sup = Scraping(sopa)
    # data = sup.extrarDataTablas()
    # for i in data:
    #     modelo = i[1].replace('Last seen: Total Earning: $   Status: Approved. Block','')
    #     cantidad = i[9].replace('$','')
    #     if float(cantidad) > 0:
    #         diaQuincena = 15 if quincena == 1 else 30
    #         db.child('imlive').child((modelo)).child(año+mes+str(quincena)).child(diaQuincena).set(str(cantidad))
     
    # browser.quit()
        
    #IMLIVE API
        
    # mesfecha=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # options = Options()
    # options.add_argument("--headless=new")
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # browser = webdriver.Chrome(options=options)
    # pagina = 'https://studio.imlive.com/#/'
    # estadistica= 'https://studio.imlive.com/#/Studio/Statistics/HostReport'
    # browser.get(pagina)
    # log = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/a/span')
    # if log is not None:
    #     log.click()
    # user = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[2]/input')
    # if user is not None:
    #     user.send_keys("olimpostudioll")
    # password = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[3]/input')
    # if password is not None:
    #     password.send_keys("Zeus2020**")
    # time.sleep(2)
    # wait = WebDriverWait(browser, 10)
    # sumbit = browser.find_element('xpath', '/html/body/nav/div/div[3]/div[2]/div/form/div[4]')
    # if sumbit is not None:
    #     sumbit.click()

    # cookies = browser.get_cookies()
    # asp_net_session_id_cokkie = None
    # for cookie in cookies:
    #     if cookie['name'] == 'ASP.NET_SessionId':
    #         asp_net_session_id_cokkie = cookie
    #         break


    # cookies = {
    #     'ASP.NET_SessionId': asp_net_session_id_cokkie['value'],  
    # }

    # browser.quit

    # validacion = True

    # while validacion:
    #     response = requests.get(
    #         f'https://studio.imlive.com/Services/ReportsService.ashx?action=hostreport&date={mesfecha[int(mes)-1]}%20{dia},%20{año}%20-%20{mesfecha[int(mes)-1]}%20{dia},%20{año}',
    #         cookies=cookies
    #     )
    #     data = response.json()
    #     if data['Data'] is not None:
    #         validacion = False
    #         for i in data['Data']:
    #             print(i['Username'])
    #             print(i['TotalEarnings'])
    #             db.child('imlive').child(i['Username']).child(año+mes+str(quincena)).child('0'+dia).set(str(i['TotalEarnings']))
    #     else:
    #         print(data['Data'])


