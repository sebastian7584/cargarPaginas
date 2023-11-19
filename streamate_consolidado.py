from selenium import webdriver
from paginas.streamate import cargarDatosStreamate
from data.dia import diaActual, diaSiguiente,hora
from data.firebaseConfig import db
import time

hr =hora()
if True:
    if int(hr) <22 :
        dia,mes,año = diaActual()
    else:
        dia,mes,año = diaSiguiente()
       


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
sumbit = browser.find_element_by_id('login-form-submit')
if sumbit is not None:
    sumbit.click()


print('Estadisticas Streamate')
mesfecha=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] 


estadistica= 'https://www.streamatemodels.com/smm/reports/earnings/EarningsReportPivot.php?range=day&earnday='+mesfecha[int(mes)-1]+'%20'+dia+',%20'+año+'&earnyear=2021&earnweek=1626480000&studio_filter=0&format=csv_summary'
browser.get(estadistica)
time.sleep(2)
browser.quit()

cargarDatosStreamate(dia,mes,año,db)




