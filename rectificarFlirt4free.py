from selenium import webdriver
from paginas.flirt4free import cargarDatosFlirt4free
from data.dia import diaActual, diaSiguiente,hora
from data.firebaseConfig import db
import time


       
for i in range (1,16):
    año ='2022'
    mes='08'
    if i < 10 :
        dia='0'+str(i)
    else : dia = i

    dia = str(dia)
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
