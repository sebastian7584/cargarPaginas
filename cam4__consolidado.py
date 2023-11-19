from data.dia import diaAnterior,diaActual,finDia
from paginas.cam4 import cargarDatosCam4
from data.firebaseConfig import db
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument('--profile-directory=Profile 3')
options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')



driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.cam4.es/')
cookies = driver.get_cookies()

driver.quit()

f = finDia()
if True:
    if f :
        d,m,a = diaAnterior()
    else:
        d,m,a = diaActual()
        
cargarDatosCam4(d,m,a,db,cookies)
