from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("chrome://settings/?search=descargas")
boton = driver.find_element('xpath', '/html/body/settings-ui//div[2]/settings-main//settings-basic-page//div[2]/settings-section[4]/settings-downloads-page//div/controlled-button//cr-button')
boton.click()

driver.close()