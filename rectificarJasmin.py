from selenium import webdriver

from data.firebaseConfig import db
import time


   


for i in range (16,32):
    año ='2023'
    mes='07'
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
    print(dia)
