import msal
import requests
import pandas as pd
from openpyxl import load_workbook
from io import BytesIO

# Función para leer el archivo de Excel directamente desde OneDrive

    


    

def main():
    # Autenticación y obtención del token de acceso
    token = get_access_token()

    # Leer el archivo de Excel directamente desde OneDrive
    df, drives_id, item_id = read_excel_from_onedrive(token)
    df['Nueva_Columna'] = 'Valor'
    file_stream = BytesIO()
    with pd.ExcelWriter(file_stream, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='resultado')

    update_excel_cell(token, drives_id, item_id, 'A3', 'ejemplo')
    # checkout_file(token, drives_id, item_id)
    # upload_excel_to_onedrive(token, file_stream, drives_id, item_id)
    # checkin_file(token, drives_id, item_id)

if __name__ == "__main__":
    main()




# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from msedge.selenium_tools import Edge, EdgeOptions

# session = requests.Session()

# cookies = {
#     'ASPSESSIONIDSSSQABQB': 'FCCPMCPDCFDKHPEIJFDACMFP',
#     'dtCookie': 'v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0',
#     'ASP.NET_SessionId': '3mxi0huvg3muxbk3gz3yj1pu',
#     'ASPSESSIONIDSCDBCARB': 'JJABNCPDHMBNFNEDFKKEOJMG',
#     'Username': '45085166',
#     'NSC_QpmjfespEjtusjX2l3': 'ffffffffaf1e1a7d45525d5f4f58455e445a4a423660',
#     '.LOGPOL': '9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
# }

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# response = session.get('https://poliedrodist.comcel.com.co/', cookies=cookies, headers=headers)


# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value

# response = session.get('https://poliedrodist.comcel.com.co/login/login.ASP', cookies=cookies, headers=headers)

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value

# # cookies = {
# #     'ASPSESSIONIDSSSQABQB': 'FCCPMCPDCFDKHPEIJFDACMFP',
# #     'dtCookie': 'v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0',
# #     'ASP.NET_SessionId': '3mxi0huvg3muxbk3gz3yj1pu',
# #     'ASPSESSIONIDSCDBCARB': 'JJABNCPDHMBNFNEDFKKEOJMG',
# #     'Username': '45085166',
# #     'NSC_QpmjfespEjtusjX2l3': 'ffffffffaf1e1a7d45525d5f4f58455e445a4a423660',
# #     '.LOGPOL': '9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
# # }

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
#     'Origin': 'https://poliedrodist.comcel.com.co',
#     'Referer': 'https://poliedrodist.comcel.com.co/login/login.ASP',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# data = {
#     'varSevr': 'poliedrodist.comcel.com.co',
# }

# response = session.post(
#     'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
#     'Origin': 'https://poliedrodist.comcel.com.co',
#     'Referer': 'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# data = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTc4NjQxODU0Nw8WAh4FcGFuZWwFFXBubFVzdWFyaW9Db250cmFzZcOxYRYCZg9kFgICAw9kFgICBQ9kFhgCBw8PZBYCHgVzdHlsZQUNZGlzcGxheTpibG9ja2QCCQ8PZBYCHwEFDGRpc3BsYXk6bm9uZWQCCw8PZBYCHwEFDGRpc3BsYXk6bm9uZWQCDQ8PZBYCHwEFDGRpc3BsYXk6bm9uZWQCDw8PZBYCHwEFDGRpc3BsYXk6bm9uZRYCAg0PD2QWAh4HT25jbGljawVLcG9wVXAoJ2h0dHBzOi8vMTk4LjIyOC45MC41NTo4MTAwL2NvbnNvbGUtc2VsZnNlcnZpY2UnKTt0aGlzLmRpc2FibGVkPXRydWU7ZAIRDw9kFgIfAQUMZGlzcGxheTpub25lZAITDw9kFgIfAQUMZGlzcGxheTpub25lFgICDQ8PZBYCHwIFS3BvcFVwKCdodHRwczovLzE5OC4yMjguOTAuNTU6ODEwMC9jb25zb2xlLXNlbGZzZXJ2aWNlJyk7dGhpcy5kaXNhYmxlZD10cnVlO2QCFQ8PZBYCHwEFDGRpc3BsYXk6bm9uZRYCAg0PD2QWAh8CBUtwb3BVcCgnaHR0cHM6Ly8xOTguMjI4LjkwLjU1OjgxMDAvY29uc29sZS1zZWxmc2VydmljZScpO3RoaXMuZGlzYWJsZWQ9dHJ1ZTtkAhcPD2QWAh8BBQxkaXNwbGF5Om5vbmVkAhkPD2QWAh8BBQxkaXNwbGF5Om5vbmVkAhsPD2QWAh8BBQxkaXNwbGF5Om5vbmVkAh0PD2QWAh8BBQxkaXNwbGF5Om5vbmVkZOVcvKA%2BH3z2IhYbGnZ%2FznBN84kI&__VIEWSTATEGENERATOR=A30FE163&__EVENTVALIDATION=%2FwEdADfX6qn5d89a%2FzRWHJ2clnKA1NFJfQ%2BpEfDZ8HEkznzgmisdeVi%2BDUoNtln8zQbxKqzlyx17sQ4qx6yfJMGZ9m9y%2Bip2pUTThEHb1yQWOKI0kZdKSRDBpmAZFx4aiYlW1fmxwHQqt9K0LvempdZtBzfKIoF4NcxrU%2BYzGk%2F3bBwBKIj5eQRMI2Scimy8ugxVyEIJumyaHSwPqu71Qr7pyG%2FGPXCKXmC0h0mg3vRW6lXQFqXxKcMDudyqp7culXBTcjJ5zNCVIhYODzYtmx2e%2FJglAX%2BFjLLLTKyo1VSEYMx80ryygWn3ENT%2BlUZoG51dlLCf0O9kg0fgrPgimoqH4Lk0Ln4gjddnAU117q386kJ72DtitpGc8Sk7ciIE7cbw9zW%2BAvTrcucO0xkHQ7GVBr0zpY3jvb1S3iPmEsHnue9bJltj0BkxzzzVREvxfuUhgiO5bDGCT5pSdHyiy03b6jDp0D4eELwOyVoJVqJFGeri74raaQaFnXKaLuO1sKRm4e%2FrHAhPrz7lBtM%2BFbvfjRSKOzYCz10ea3hqopOdQ5HEhAfVrr6HY7rImeXT7qimi5CRr0OajTqbb2b8dzg5%2BzzNNOWwlCLkP9Zpqa9oiLWk8NakgzlJEfGonIrPIZ%2F6lLGsXDBWqtXFJp1hNFgbxbZt%2BHJ8sjHcK%2Bz%2FUH50AHGlD2wSYd%2FpVGYisDRwwLiXvSHcF4k4CnfMYNJ1wpPfZx4rbXWV%2FYdlA9FzSfObBkuPcVDpzqlg2bn3nJq5S4QyHRkZMepEyui%2FHDlMyd2rlgjWfswnhOle5huuRV23Cx%2BFaaMS1Y%2BK9VDnzGXxkf37hS8l%2FXXwAZwr29KQ8t73hFln6e3kIsUT3RH8XkeGUuG6FWfg%2BS6kEvKQRtfAykPT4CYMnzWOArwGyMCpoJhZXLpwi9ueOAgmatprbpnnHQcAyraGUPw8wt97%2F%2FLRsg4kCulsMMNpA4o60hiys6w65rIif0b6dP6AOuXsUKgk25mj2UhKirtC%2BdrnRekj7A3Lf7W4kez1oOweb6ZFFx9zpp%2FeHo9TQjV%2FbG1KbHE7MIt5GU%2BkJqOihs13Gb9pDhdN6N%2F%2BkDdcwDZCQeyq9LCu8J7Lq7bQU5y9Kg53iLqQvuxtfldKBuiH0n4yi1TC6%2FrT3JhJJOIuicza%2BOA4FRAZOmrrwyJwoKg6cPWRnyXhxDDT2zqlRNA%3D&ctl00%24ContentPlaceHolder1%24hdnClientPublicIP=186.121.9.175&ctl00%24ContentPlaceHolder1%24hdnIdToken=0&ctl00%24ContentPlaceHolder1%24hdnDetectIdCollectData=%7B%22flashVars%22%3A%7B%7D%2C%22flashFonts%22%3A%5B%5D%2C%22jsFonts%22%3A%5B%22.Aqua+Kana+Bold%22%2C%22.Aqua+Kana%22%2C%22.Helvetica+LT+MM%22%2C%22.Helvetica+Neue+Desk+UI+Bold+Italic%22%2C%22.Helvetica+Neue+Desk+UI+Bold%22%2C%22.Helvetica+Neue+Desk+UI+Italic%22%2C%22.Helvetica+Neue+Desk+UI%22%2C%22.Keyboard%22%2C%22.Times+LT+MM%22%2C%22Apple+Braille+Outline+6+Dot%22%2C%22Apple+Braille+Outline+8+Dot%22%2C%22Apple+Braille+Pinpoint+6+Dot%22%2C%22Apple+Braille+Pinpoint+8+Dot%22%2C%22Arial+Black%22%2C%22Arial+Narrow%22%2C%22Arial%22%2C%22Calibri+Light%22%2C%22Calibri%22%2C%22Cambria+Math%22%2C%22Cambria%22%2C%22Candara%22%2C%22Comic+Sans+MS%22%2C%22Consolas%22%2C%22Constantia%22%2C%22Corbel%22%2C%22Courier+10+Pitch+Italic%22%2C%22Courier+10+Pitch%22%2C%22Courier+New%22%2C%22Courier%22%2C%22Ebrima%22%2C%22Franklin+Gothic+Medium%22%2C%22Gabriola%22%2C%22Gadugi%22%2C%22Georgia%22%2C%22Helvetica%22%2C%22Impact%22%2C%22Leelawadee%22%2C%22Lucida+Console%22%2C%22Lucida+Sans+Unicode%22%2C%22Malgun+Gothic%22%2C%22Marlett%22%2C%22Microsoft+Himalaya%22%2C%22Microsoft+JhengHei+UI%22%2C%22Microsoft+JhengHei%22%2C%22Microsoft+New+Tai+Lue%22%2C%22Microsoft+PhagsPa%22%2C%22Microsoft+Sans+Serif%22%2C%22Microsoft+Tai+Le%22%2C%22Microsoft+Uighur%22%2C%22Microsoft+YaHei+UI%22%2C%22Microsoft+YaHei%22%2C%22Microsoft+Yi+Baiti%22%2C%22MingLiU-ExtB%22%2C%22MingLiU_HKSCS-ExtB%22%2C%22Mongolian+Baiti%22%2C%22MS+Gothic%22%2C%22MS+PGothic%22%2C%22MS+UI+Gothic%22%2C%22MV+Boli%22%2C%22Myanmar+Text%22%2C%22Nirmala+UI%22%2C%22NSimSun%22%2C%22Palatino+Linotype%22%2C%22Papyrus+Condensed%22%2C%22Papyrus%22%2C%22PMingLiU-ExtB%22%2C%22Segoe+Print%22%2C%22Segoe+Script%22%2C%22Segoe+UI+Light%22%2C%22Segoe+UI+Semibold%22%2C%22Segoe+UI+Symbol%22%2C%22Segoe+UI%22%2C%22SimSun%22%2C%22SimSun-ExtB%22%2C%22Sylfaen%22%2C%22Symbol%22%2C%22Tahoma%22%2C%22Trebuchet+MS%22%2C%22Verdana%22%2C%22Webdings%22%2C%22Wingdings+2%22%2C%22Wingdings+3%22%2C%22Wingdings%22%2C%22Wingdings%22%5D%2C%22documentFeatures%22%3A%7B%22HTML%22%3Atrue%2C%22HTML-3.0%22%3Atrue%2C%22HTML-4.0%22%3Atrue%2C%22XML%22%3Atrue%2C%22XML-3.0%22%3Atrue%2C%22XML-4.0%22%3Atrue%2C%22Views%22%3Atrue%2C%22Views-1.0%22%3Atrue%2C%22Views-2.0%22%3Atrue%2C%22Views-3.0%22%3Atrue%2C%22Views-4.0%22%3Atrue%2C%22StyleSheets%22%3Atrue%2C%22StyleSheets-1.0%22%3Atrue%2C%22StyleSheets-2.0%22%3Atrue%2C%22StyleSheets-3.0%22%3Atrue%2C%22StyleSheets-4.0%22%3Atrue%2C%22CSS%22%3Atrue%2C%22CSS-1.0%22%3Atrue%2C%22CSS-2.0%22%3Atrue%2C%22CSS-3.0%22%3Atrue%2C%22CSS-4.0%22%3Atrue%2C%22CSS2%22%3Atrue%2C%22CSS2-1.0%22%3Atrue%2C%22CSS2-2.0%22%3Atrue%2C%22CSS2-3.0%22%3Atrue%2C%22CSS2-4.0%22%3Atrue%2C%22Events%22%3Atrue%2C%22Events-1.0%22%3Atrue%2C%22Events-2.0%22%3Atrue%2C%22Events-3.0%22%3Atrue%2C%22Events-4.0%22%3Atrue%2C%22UIEvents%22%3Atrue%2C%22UIEvents-1.0%22%3Atrue%2C%22UIEvents-2.0%22%3Atrue%2C%22UIEvents-3.0%22%3Atrue%2C%22UIEvents-4.0%22%3Atrue%2C%22MouseEvents%22%3Atrue%2C%22MouseEvents-1.0%22%3Atrue%2C%22MouseEvents-2.0%22%3Atrue%2C%22MouseEvents-3.0%22%3Atrue%2C%22MouseEvents-4.0%22%3Atrue%2C%22MutationEvents%22%3Atrue%2C%22MutationEvents-1.0%22%3Atrue%2C%22MutationEvents-2.0%22%3Atrue%2C%22MutationEvents-3.0%22%3Atrue%2C%22MutationEvents-4.0%22%3Atrue%2C%22HTMLEvents%22%3Atrue%2C%22HTMLEvents-1.0%22%3Atrue%2C%22HTMLEvents-2.0%22%3Atrue%2C%22HTMLEvents-3.0%22%3Atrue%2C%22HTMLEvents-4.0%22%3Atrue%2C%22Traversal%22%3Atrue%2C%22Traversal-1.0%22%3Atrue%2C%22Traversal-2.0%22%3Atrue%2C%22Traversal-3.0%22%3Atrue%2C%22Traversal-4.0%22%3Atrue%2C%22Range%22%3Atrue%2C%22Range-1.0%22%3Atrue%2C%22Range-2.0%22%3Atrue%2C%22Range-3.0%22%3Atrue%2C%22Range-4.0%22%3Atrue%7D%2C%22mimeTypes%22%3A%5B%7B%22type%22%3A%22application%2Fpdf%22%2C%22description%22%3A%22Portable+Document+Format%22%2C%22suffixes%22%3A%22pdf%22%7D%2C%7B%22type%22%3A%22text%2Fpdf%22%2C%22description%22%3A%22Portable+Document+Format%22%2C%22suffixes%22%3A%22pdf%22%7D%5D%2C%22plugins%22%3A%5B%7B%22name%22%3A%22Chrome+PDF+Viewer%22%2C%22description%22%3A%22df8b8a3c2e9816c8fa5785b811006754%22%2C%22filename%22%3A%22internal-pdf-viewer%22%7D%2C%7B%22name%22%3A%22Chromium+PDF+Viewer%22%2C%22description%22%3A%22df8b8a3c2e9816c8fa5785b811006754%22%2C%22filename%22%3A%22internal-pdf-viewer%22%7D%2C%7B%22name%22%3A%22Microsoft+Edge+PDF+Viewer%22%2C%22description%22%3A%22df8b8a3c2e9816c8fa5785b811006754%22%2C%22filename%22%3A%22internal-pdf-viewer%22%7D%2C%7B%22name%22%3A%22PDF+Viewer%22%2C%22description%22%3A%22df8b8a3c2e9816c8fa5785b811006754%22%2C%22filename%22%3A%22internal-pdf-viewer%22%7D%2C%7B%22name%22%3A%22WebKit+built-in+PDF%22%2C%22description%22%3A%22df8b8a3c2e9816c8fa5785b811006754%22%2C%22filename%22%3A%22internal-pdf-viewer%22%7D%5D%2C%22jsGeneralData%22%3A%7B%22activex%22%3Afalse%2C%22adobeReader%22%3Afalse%2C%22XMLHttpRequest%22%3A%22+via+XMLHttpRequest+object%22%2C%22XMLSerializer%22%3Atrue%2C%22AjaxXMLParser%22%3A%22+via+DOMParser%22%2C%22navigator_appName%22%3A%22Netscape%22%2C%22navigator_appCodeName%22%3A%22Mozilla%22%2C%22navigator_appVersion%22%3A%225.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F128.0.0.0+Safari%2F537.36%22%2C%22navigator_appMinorVersion%22%3Afalse%2C%22navigator_vendor%22%3A%22Google+Inc.%22%2C%22navigator_userAgent%22%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F128.0.0.0+Safari%2F537.36%22%2C%22navigator_oscpu%22%3Afalse%2C%22navigator_platform%22%3A%22Win32%22%2C%22navigator_securityPolicy%22%3Afalse%2C%22navigator_onLine%22%3Atrue%2C%22browser_name%22%3A%22chrome%22%2C%22browser_version%22%3A%22128.0.0.0%22%2C%22layout_name%22%3A%22webkit%22%2C%22layout_version%22%3A%22537.36%22%2C%22os_name%22%3A%22win%22%2C%22IEVersion%22%3Afalse%2C%22cookieEnabled%22%3Atrue%2C%22CPU%22%3Afalse%2C%22document_defaultCharset%22%3Afalse%2C%22dotNetFramework%22%3A%22%22%2C%22flashVersion%22%3Afalse%2C%22google_gears%22%3Afalse%2C%22geckoProduct%22%3A%22Gecko+20030107%22%2C%22geckoVendor%22%3A%22%22%2C%22isMozilla%22%3Afalse%2C%22isGoogleChrome%22%3Atrue%2C%22googleChromeVersion%22%3A128%2C%22googleChromeLayout%22%3A%22webkit5%22%2C%22navigator_language%22%3A%22es-ES%22%2C%22navigator_systemLanguage%22%3Afalse%2C%22navigator_userLanguage%22%3Afalse%2C%22navigator_browserLanguage%22%3Afalse%2C%22openOfficePlugIn%22%3Afalse%2C%22isOpera%22%3Afalse%2C%22operaVersion%22%3Afalse%2C%22operaLayout%22%3Afalse%2C%22SVGViewer%22%3Afalse%2C%22citrix%22%3Afalse%2C%22SunJavaPlugin%22%3Atrue%2C%22MicrosoftScriptControl%22%3Afalse%2C%22crypto_version%22%3Afalse%2C%22QuickTimePlayer%22%3Afalse%2C%22RealOne%22%3Afalse%2C%22RealOneComponents%22%3Afalse%2C%22RealPlayer%22%3Afalse%2C%22RealPlayerG2%22%3Afalse%2C%22RealJukebox%22%3Afalse%2C%22screen_width%22%3A1920%2C%22screen_height%22%3A1080%2C%22screen_deviceXDPI%22%3Afalse%2C%22screen_deviceYDPI%22%3Afalse%2C%22screen_logicalXDPI%22%3Afalse%2C%22screen_logicalYDPI%22%3Afalse%2C%22screen_pixelDepth%22%3A24%2C%22screen_colorDepth%22%3A24%2C%22screen_fontSmoothingEnabled%22%3Afalse%2C%22screen_updateInterval%22%3Afalse%2C%22screen_bufferDepth%22%3Afalse%2C%22AdobeShockwave%22%3Afalse%2C%22Silverlight_supportedUserAgent%22%3Afalse%2C%22WebKit%22%3A%22537.36%22%2C%22WebKitNightlyBuild%22%3A%22No%22%2C%22WebKitBrowserName%22%3A%22Google+Chrome+128.0.0.0%22%2C%22WebKitMobileDevice%22%3Afalse%2C%22window_offscreenBuffering%22%3Afalse%2C%22timezoneOffset%22%3A300%7D%2C%22canvas%22%3A%2222d44bd4e8533344e28a4545aff6ad2a121a3375280557ab251f268ab9a42857ba5cd4829091afbd419fc857ed0a1659a33cc564a07e5fe72b4f915db031ddc7%23%23%23%23%22%2C%22osStyleColors%22%3A%7B%22ActiveBorder%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22ActiveCaption%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22AppWorkspace%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22Background%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22ButtonFace%22%3A%22rgb%28240%2C+240%2C+240%29%22%2C%22ButtonHighlight%22%3A%22rgb%28240%2C+240%2C+240%29%22%2C%22ButtonShadow%22%3A%22rgb%28240%2C+240%2C+240%29%22%2C%22ButtonText%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22CaptionText%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22GrayText%22%3A%22rgb%28109%2C+109%2C+109%29%22%2C%22Highlight%22%3A%22rgb%280%2C+120%2C+215%29%22%2C%22HighlightText%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22InactiveBorder%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22InactiveCaption%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22InactiveCaptionText%22%3A%22rgb%28128%2C+128%2C+128%29%22%2C%22InfoBackground%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22InfoText%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22Menu%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22MenuText%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22Scrollbar%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22ThreeDDarkShadow%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22ThreeDFace%22%3A%22rgb%28240%2C+240%2C+240%29%22%2C%22ThreeDHighlight%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22ThreeDLightShadow%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22ThreeDShadow%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22Window%22%3A%22rgb%28255%2C+255%2C+255%29%22%2C%22WindowFrame%22%3A%22rgb%280%2C+0%2C+0%29%22%2C%22WindowText%22%3A%22rgb%280%2C+0%2C+0%29%22%7D%7D&ctl00%24ContentPlaceHolder1%24txtUsuario=45085166&ctl00%24ContentPlaceHolder1%24txtContrase%C3%B1a=Julio*%2F*26&ctl00%24ContentPlaceHolder1%24btnIngresarUsuarioContrase%C3%B1a=Ingresar+%EE%A4%8D&ctl00%24ContentPlaceHolder1%24txtUserCC=&ctl00%24ContentPlaceHolder1%24txtACCC=&ctl00%24ContentPlaceHolder1%24txtNC1CC=&ctl00%24ContentPlaceHolder1%24txtNC2CC=&ctl00%24ContentPlaceHolder1%24txt_passActualOld=&ctl00%24ContentPlaceHolder1%24txt_NewPassAlg=&ctl00%24ContentPlaceHolder1%24txt_NewPassAlgConfir=&ctl00%24ContentPlaceHolder1%24txtClaveNueva=&ctl00%24ContentPlaceHolder1%24txtConfirmaClave=&ctl00%24ContentPlaceHolder1%24txtConL3=&ctl00%24ContentPlaceHolder1%24ClaOcu=&ctl00%24ContentPlaceHolder1%24txtNewPin=&ctl00%24ContentPlaceHolder1%24ClaPin=&ctl00%24ContentPlaceHolder1%24txtNewToken=&ctl00%24ContentPlaceHolder1%24ClaToken=&ctl00%24ContentPlaceHolder1%24txtTokenDetectId=&ctl00%24ContentPlaceHolder1%24txtTipoNuevoParAuth=&ctl00%24ContentPlaceHolder1%24txt_deviceIdClient=&ctl00%24ContentPlaceHolder1%24txt_tranactionId=&ctl00%24ContentPlaceHolder1%24hdnTokenEntrust=&ctl00%24ContentPlaceHolder1%24txtTokenEntrust='

# response = session.post(
#     'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value

# token = input('token: ')

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=9A53BFA68533E3F477FD634C1BD943D149CC503728C8AA2A8F203ACAF3A243B62FBFC0B9658EAFFC975B964679D1AFDC20E0E771B59A8480A2E198DD11879B0B6A746616535A15C0A3B834A8C805979C1AFF8044665D91EAEB1CD44BE7CB6F84067B226472B258C1C22512F2B131AEC80F13CFC1',
#     'Origin': 'https://poliedrodist.comcel.com.co',
#     'Referer': 'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# data = {
#     '__EVENTTARGET': '',
#     '__EVENTARGUMENT': '',
#     '__VIEWSTATE': '/wEPDwUKLTc4NjQxODU0Nw8WBB4FcGFuZWwFD3BubFRva2VuRW50cnVzdB4HTWVuc2FqZQUXwqFBY2Nlc28gTm8gcGVybWl0aWRvIS4WAmYPZBYCAgMPZBYCAgUPZBYYAgcPD2QWAh4Fc3R5bGUFDGRpc3BsYXk6bm9uZWQCCQ8PZBYCHwIFDGRpc3BsYXk6bm9uZWQCCw8PZBYCHwIFDGRpc3BsYXk6bm9uZWQCDQ8PZBYCHwIFDGRpc3BsYXk6bm9uZWQCDw8PZBYCHwIFDGRpc3BsYXk6bm9uZRYCAg0PD2QWAh4HT25jbGljawVLcG9wVXAoJ2h0dHBzOi8vMTk4LjIyOC45MC41NTo4MTAwL2NvbnNvbGUtc2VsZnNlcnZpY2UnKTt0aGlzLmRpc2FibGVkPXRydWU7ZAIRDw9kFgIfAgUMZGlzcGxheTpub25lFgICAQ8PFgYeCUZvbnRfU2l6ZSgqIlN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuRm9udFVuaXQEMTZwdB4EVGV4dAUXwqFBY2Nlc28gTm8gcGVybWl0aWRvIS4eBF8hU0ICgAhkZAITDw9kFgIfAgUMZGlzcGxheTpub25lFgICDQ8PZBYCHwMFS3BvcFVwKCdodHRwczovLzE5OC4yMjguOTAuNTU6ODEwMC9jb25zb2xlLXNlbGZzZXJ2aWNlJyk7dGhpcy5kaXNhYmxlZD10cnVlO2QCFQ8PZBYCHwIFDGRpc3BsYXk6bm9uZRYCAg0PD2QWAh8DBUtwb3BVcCgnaHR0cHM6Ly8xOTguMjI4LjkwLjU1OjgxMDAvY29uc29sZS1zZWxmc2VydmljZScpO3RoaXMuZGlzYWJsZWQ9dHJ1ZTtkAhcPD2QWAh8CBQxkaXNwbGF5Om5vbmVkAhkPD2QWAh8CBQxkaXNwbGF5Om5vbmVkAhsPD2QWAh8CBQxkaXNwbGF5Om5vbmVkAh0PD2QWAh8CBQ1kaXNwbGF5OmJsb2NrFgICAw8PFgIfBQUINDUwODUxNjZkZGRUR6/FstPEu39xAlUSTGNoUti4fw==',
#     '__VIEWSTATEGENERATOR': 'A30FE163',
#     '__EVENTVALIDATION': '/wEdADcorxP+y8MRvzDcCS5XLgrn1NFJfQ+pEfDZ8HEkznzgmisdeVi+DUoNtln8zQbxKqzlyx17sQ4qx6yfJMGZ9m9y+ip2pUTThEHb1yQWOKI0kZdKSRDBpmAZFx4aiYlW1fmxwHQqt9K0LvempdZtBzfKIoF4NcxrU+YzGk/3bBwBKIj5eQRMI2Scimy8ugxVyEIJumyaHSwPqu71Qr7pyG/GPXCKXmC0h0mg3vRW6lXQFqXxKcMDudyqp7culXBTcjJ5zNCVIhYODzYtmx2e/JglAX+FjLLLTKyo1VSEYMx80ryygWn3ENT+lUZoG51dlLCf0O9kg0fgrPgimoqH4Lk0Ln4gjddnAU117q386kJ72DtitpGc8Sk7ciIE7cbw9zW+AvTrcucO0xkHQ7GVBr0zpY3jvb1S3iPmEsHnue9bJltj0BkxzzzVREvxfuUhgiO5bDGCT5pSdHyiy03b6jDp0D4eELwOyVoJVqJFGeri74raaQaFnXKaLuO1sKRm4e/rHAhPrz7lBtM+FbvfjRSKOzYCz10ea3hqopOdQ5HEhAfVrr6HY7rImeXT7qimi5CRr0OajTqbb2b8dzg5+zzNNOWwlCLkP9Zpqa9oiLWk8NakgzlJEfGonIrPIZ/6lLGsXDBWqtXFJp1hNFgbxbZt+HJ8sjHcK+z/UH50AHGlD2wSYd/pVGYisDRwwLiXvSHcF4k4CnfMYNJ1wpPfZx4rbXWV/YdlA9FzSfObBkuPcVDpzqlg2bn3nJq5S4QyHRkZMepEyui/HDlMyd2rlgjWfswnhOle5huuRV23Cx+FaaMS1Y+K9VDnzGXxkf37hS8l/XXwAZwr29KQ8t73hFln6e3kIsUT3RH8XkeGUuG6FWfg+S6kEvKQRtfAykPT4CYMnzWOArwGyMCpoJhZXLpwi9ueOAgmatprbpnnHQcAyraGUPw8wt97//LRsg4kCulsMMNpA4o60hiys6w65rIif0b6dP6AOuXsUKgk25mj2UhKirtC+drnRekj7A3Lf7W4kez1oOweb6ZFFx9zpp/eHo9TQjV/bG1KbHE7MIt5GU+kJqOihs13Gb9pDhdN6N/+kDdcwDZCQeyq9LCu8J7Lq7bQU5y9Kg53iLqQvuxtfldKBuiH0n4yi1TC6/rT3JhJJOIuicza+OA4FRAZOmrrF6mJ2dbPl+yCb+ur30a4ZyhKudg=',
#     'ctl00$ContentPlaceHolder1$hdnClientPublicIP': '186.121.9.175',
#     'ctl00$ContentPlaceHolder1$hdnIdToken': '0',
#     'ctl00$ContentPlaceHolder1$hdnDetectIdCollectData': '{"flashVars":{},"flashFonts":[],"jsFonts":[".Aqua Kana Bold",".Aqua Kana",".Helvetica LT MM",".Helvetica Neue Desk UI Bold Italic",".Helvetica Neue Desk UI Bold",".Helvetica Neue Desk UI Italic",".Helvetica Neue Desk UI",".Keyboard",".Times LT MM","Apple Braille Outline 6 Dot","Apple Braille Outline 8 Dot","Apple Braille Pinpoint 6 Dot","Apple Braille Pinpoint 8 Dot","Arial Black","Arial Narrow","Arial","Calibri Light","Calibri","Cambria Math","Cambria","Candara","Comic Sans MS","Consolas","Constantia","Corbel","Courier 10 Pitch Italic","Courier 10 Pitch","Courier New","Courier","Ebrima","Franklin Gothic Medium","Gabriola","Gadugi","Georgia","Helvetica","Impact","Leelawadee","Lucida Console","Lucida Sans Unicode","Malgun Gothic","Marlett","Microsoft Himalaya","Microsoft JhengHei UI","Microsoft JhengHei","Microsoft New Tai Lue","Microsoft PhagsPa","Microsoft Sans Serif","Microsoft Tai Le","Microsoft Uighur","Microsoft YaHei UI","Microsoft YaHei","Microsoft Yi Baiti","MingLiU-ExtB","MingLiU_HKSCS-ExtB","Mongolian Baiti","MS Gothic","MS PGothic","MS UI Gothic","MV Boli","Myanmar Text","Nirmala UI","NSimSun","Palatino Linotype","Papyrus Condensed","Papyrus","PMingLiU-ExtB","Segoe Print","Segoe Script","Segoe UI Light","Segoe UI Semibold","Segoe UI Symbol","Segoe UI","SimSun","SimSun-ExtB","Sylfaen","Symbol","Tahoma","Trebuchet MS","Verdana","Webdings","Wingdings 2","Wingdings 3","Wingdings","Wingdings"],"documentFeatures":{"HTML":true,"HTML-3.0":true,"HTML-4.0":true,"XML":true,"XML-3.0":true,"XML-4.0":true,"Views":true,"Views-1.0":true,"Views-2.0":true,"Views-3.0":true,"Views-4.0":true,"StyleSheets":true,"StyleSheets-1.0":true,"StyleSheets-2.0":true,"StyleSheets-3.0":true,"StyleSheets-4.0":true,"CSS":true,"CSS-1.0":true,"CSS-2.0":true,"CSS-3.0":true,"CSS-4.0":true,"CSS2":true,"CSS2-1.0":true,"CSS2-2.0":true,"CSS2-3.0":true,"CSS2-4.0":true,"Events":true,"Events-1.0":true,"Events-2.0":true,"Events-3.0":true,"Events-4.0":true,"UIEvents":true,"UIEvents-1.0":true,"UIEvents-2.0":true,"UIEvents-3.0":true,"UIEvents-4.0":true,"MouseEvents":true,"MouseEvents-1.0":true,"MouseEvents-2.0":true,"MouseEvents-3.0":true,"MouseEvents-4.0":true,"MutationEvents":true,"MutationEvents-1.0":true,"MutationEvents-2.0":true,"MutationEvents-3.0":true,"MutationEvents-4.0":true,"HTMLEvents":true,"HTMLEvents-1.0":true,"HTMLEvents-2.0":true,"HTMLEvents-3.0":true,"HTMLEvents-4.0":true,"Traversal":true,"Traversal-1.0":true,"Traversal-2.0":true,"Traversal-3.0":true,"Traversal-4.0":true,"Range":true,"Range-1.0":true,"Range-2.0":true,"Range-3.0":true,"Range-4.0":true},"mimeTypes":[{"type":"application/pdf","description":"Portable Document Format","suffixes":"pdf"},{"type":"text/pdf","description":"Portable Document Format","suffixes":"pdf"}],"plugins":[{"name":"Chrome PDF Viewer","description":"df8b8a3c2e9816c8fa5785b811006754","filename":"internal-pdf-viewer"},{"name":"Chromium PDF Viewer","description":"df8b8a3c2e9816c8fa5785b811006754","filename":"internal-pdf-viewer"},{"name":"Microsoft Edge PDF Viewer","description":"df8b8a3c2e9816c8fa5785b811006754","filename":"internal-pdf-viewer"},{"name":"PDF Viewer","description":"df8b8a3c2e9816c8fa5785b811006754","filename":"internal-pdf-viewer"},{"name":"WebKit built-in PDF","description":"df8b8a3c2e9816c8fa5785b811006754","filename":"internal-pdf-viewer"}],"jsGeneralData":{"activex":false,"adobeReader":false,"XMLHttpRequest":" via XMLHttpRequest object","XMLSerializer":true,"AjaxXMLParser":" via DOMParser","navigator_appName":"Netscape","navigator_appCodeName":"Mozilla","navigator_appVersion":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36","navigator_appMinorVersion":false,"navigator_vendor":"Google Inc.","navigator_userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36","navigator_oscpu":false,"navigator_platform":"Win32","navigator_securityPolicy":false,"navigator_onLine":true,"browser_name":"chrome","browser_version":"128.0.0.0","layout_name":"webkit","layout_version":"537.36","os_name":"win","IEVersion":false,"cookieEnabled":true,"CPU":false,"document_defaultCharset":false,"dotNetFramework":"","flashVersion":false,"google_gears":false,"geckoProduct":"Gecko 20030107","geckoVendor":"","isMozilla":false,"isGoogleChrome":true,"googleChromeVersion":128,"googleChromeLayout":"webkit5","navigator_language":"es-ES","navigator_systemLanguage":false,"navigator_userLanguage":false,"navigator_browserLanguage":false,"openOfficePlugIn":false,"isOpera":false,"operaVersion":false,"operaLayout":false,"SVGViewer":false,"citrix":false,"SunJavaPlugin":true,"MicrosoftScriptControl":false,"crypto_version":false,"QuickTimePlayer":false,"RealOne":false,"RealOneComponents":false,"RealPlayer":false,"RealPlayerG2":false,"RealJukebox":false,"screen_width":1920,"screen_height":1080,"screen_deviceXDPI":false,"screen_deviceYDPI":false,"screen_logicalXDPI":false,"screen_logicalYDPI":false,"screen_pixelDepth":24,"screen_colorDepth":24,"screen_fontSmoothingEnabled":false,"screen_updateInterval":false,"screen_bufferDepth":false,"AdobeShockwave":false,"Silverlight_supportedUserAgent":false,"WebKit":"537.36","WebKitNightlyBuild":"No","WebKitBrowserName":"Google Chrome 128.0.0.0","WebKitMobileDevice":false,"window_offscreenBuffering":false,"timezoneOffset":300},"canvas":"22d44bd4e8533344e28a4545aff6ad2a121a3375280557ab251f268ab9a42857ba5cd4829091afbd419fc857ed0a1659a33cc564a07e5fe72b4f915db031ddc7####","osStyleColors":{"ActiveBorder":"rgb(0, 0, 0)","ActiveCaption":"rgb(0, 0, 0)","AppWorkspace":"rgb(255, 255, 255)","Background":"rgb(255, 255, 255)","ButtonFace":"rgb(240, 240, 240)","ButtonHighlight":"rgb(240, 240, 240)","ButtonShadow":"rgb(240, 240, 240)","ButtonText":"rgb(0, 0, 0)","CaptionText":"rgb(0, 0, 0)","GrayText":"rgb(109, 109, 109)","Highlight":"rgb(0, 120, 215)","HighlightText":"rgb(255, 255, 255)","InactiveBorder":"rgb(0, 0, 0)","InactiveCaption":"rgb(255, 255, 255)","InactiveCaptionText":"rgb(128, 128, 128)","InfoBackground":"rgb(255, 255, 255)","InfoText":"rgb(0, 0, 0)","Menu":"rgb(255, 255, 255)","MenuText":"rgb(0, 0, 0)","Scrollbar":"rgb(255, 255, 255)","ThreeDDarkShadow":"rgb(0, 0, 0)","ThreeDFace":"rgb(240, 240, 240)","ThreeDHighlight":"rgb(0, 0, 0)","ThreeDLightShadow":"rgb(0, 0, 0)","ThreeDShadow":"rgb(0, 0, 0)","Window":"rgb(255, 255, 255)","WindowFrame":"rgb(0, 0, 0)","WindowText":"rgb(0, 0, 0)"}}',
#     'ctl00$ContentPlaceHolder1$txtUsuario': '45085166',
#     'ctl00$ContentPlaceHolder1$txtContraseña': 'Julio*/*26',
#     'ctl00$ContentPlaceHolder1$txtUserCC': '',
#     'ctl00$ContentPlaceHolder1$txtACCC': '',
#     'ctl00$ContentPlaceHolder1$txtNC1CC': '',
#     'ctl00$ContentPlaceHolder1$txtNC2CC': '',
#     'ctl00$ContentPlaceHolder1$txt_passActualOld': '',
#     'ctl00$ContentPlaceHolder1$txt_NewPassAlg': '',
#     'ctl00$ContentPlaceHolder1$txt_NewPassAlgConfir': '',
#     'ctl00$ContentPlaceHolder1$txtClaveNueva': '',
#     'ctl00$ContentPlaceHolder1$txtConfirmaClave': '',
#     'ctl00$ContentPlaceHolder1$txtConL3': '',
#     'ctl00$ContentPlaceHolder1$ClaOcu': '',
#     'ctl00$ContentPlaceHolder1$txtNewPin': '',
#     'ctl00$ContentPlaceHolder1$ClaPin': '',
#     'ctl00$ContentPlaceHolder1$txtNewToken': '',
#     'ctl00$ContentPlaceHolder1$ClaToken': '',
#     'ctl00$ContentPlaceHolder1$txtTokenDetectId': '',
#     'ctl00$ContentPlaceHolder1$txtTipoNuevoParAuth': '',
#     'ctl00$ContentPlaceHolder1$txt_deviceIdClient': '',
#     'ctl00$ContentPlaceHolder1$txt_tranactionId': '',
#     'ctl00$ContentPlaceHolder1$hdnTokenEntrust': 'GPEAkbOVxYfkRxldmFK7DRYfipxSCFvucNZfOWf0ktCNFRPmscdxywOEz3MthlND3QzAGW4cUSRrUBU4idnPtz/PPPdEeWDyF6V7JhTEYaIzdU5HOIFuHRXh7ZavOyg1SeOkjZfXZyrNQZ5bTvcmuTPBbnENe1tRc1q95e9bjFxILL8DTr/0Oy2RBrY6Rv98Q0aX2DbxhdZrkrzYA3lpq4CnDBJX9euvUljOMhUkJ96uD4cPYwD9e+5AI5l1ANBftF386HBjyndOen2PvfxoQDmDmSEF0yy8UaArXcZqbsGM7IrE/5u+z1PY3yNqS9uGz9E66hjXvxWuGHJmtrAa3ewlbLkY8WS6Ku8RCfp/Rsp63HIhqi9rlXWZ5IRqkGDkvQ/22JNBKCVoKjOx7LKhg+OK50MmZktbMmdDlSYbyucz0grU3QNjTsNPQlygQ6TSDFYVita7BZy73YKz5O8ZlZsHDaDeQ7IDaJqvN1hh/nLqrFW8kRJqGUOKMo8StyQBCurPZjeCdNFuSJY0sDso4jfGUkCx/fMWyjALt23tmMMuP0HZliMmtL/VxIDtcv0pVgHZT88+A2JBZPm385C9pIvPwoS1lm6h6XLEzRkn7lAa3bhF3bc56wQGhp+Vwl5ZADQPiE7EjKz4jZJYlFGR8ZqteXj5jexAkO5nXeqS4ivi5I7s5qyavCyMb9ytBHsQe/6JC3VN5QVjTnN8lpF8TOB1nRAu86bpI+hxwhBhktLccNqppuWepI07OESpesOSAWp1FKsA0lK9oJU4zHc+hraXQIeImzv3ecTiMceYxWMB6T/+TM7jZQ8XwOUxEwu1eA==',
#     'ctl00$ContentPlaceHolder1$txtTokenEntrust': token,
#     'ctl00$ContentPlaceHolder1$BtnLoginTokenEntrust': 'Ingresar',
# }

# response = session.post(
#     'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=48DECE43CAB3B4E2780F5A56062B015AC1B7A93BEC0CA2D59BCE26536776FBD0DDF9E4A390202F3D2CB78D8B22ADA09B2B2ED5C613DA064B2BA66ADBEC15A285258BC22611729DABE341E409A97DD5A31D8681A11C0C9768B3373D884C2A4B76934A3B8F425ED642A55627703142E825BC32879F',
#     'Referer': 'https://poliedrodist.comcel.com.co/LoginPoliedro/Login.aspx',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# response = session.get(
#     'https://poliedrodist.comcel.com.co/LoginPoliedro/LogonDispacher.aspx',
#     cookies=cookies,
#     headers=headers,
# )

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=48DECE43CAB3B4E2780F5A56062B015AC1B7A93BEC0CA2D59BCE26536776FBD0DDF9E4A390202F3D2CB78D8B22ADA09B2B2ED5C613DA064B2BA66ADBEC15A285258BC22611729DABE341E409A97DD5A31D8681A11C0C9768B3373D884C2A4B76934A3B8F425ED642A55627703142E825BC32879F',
#     'Origin': 'https://poliedrodist.comcel.com.co',
#     'Referer': 'https://poliedrodist.comcel.com.co/LoginPoliedro/LogonDispacher.aspx',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# data = {
#     'DESC': '5B57515E5D5B4757505C520E064D5A52545D5F5F4756555D460B054F535D434353575709034A5E58555B555F57520B014B58426C5B5542435A59500F6079787A757A636476777F6767647A4B5640436944415F450A0C0F15190F000D070C040900630F720D70610A7165750F7060660C7E097C630F750D630C616008670F610D61670A6B0875627D0D4F5154516C55585240560A04001F07050A01010503000104060104010503000104060104010503000104060104010503000104485059575E565D0E72060202051901020306064F5547455D6D505A5545530E074D47404355415F5C684357570B0006060B020004054A464642526847535F5F5052555A585F6D4057440E194056411D4453561C4A50585547404355415F5C0A0507030E010200054B52575D42465C555C44455D400B797672767B7D7B7D4A4656515A585F0F014A5D5769435243545A5A094F585C5A5340560B6076777E17727D7E7B617D7F7076657B7C786713651D76111F13776472646776757D1C777A677F7C66647B724A5546425659455B50570966776C677E7E4F465141505A5B6E425F43470E024F4358425C694140435245585D0E03',
#     'AUDI': '5A526745505C405757505F5C590C0300070404060B00094E47595F56580E034D',
#     'Token': 'yoHjZkr6KnyjhUCEHgnFZQ==:1d2LzvmisZI/puCYQ7n05HAd/PT9MScBfbKzWX/puGzXFKY4BqCpi57iM1P0J7dBTRzDG6rJZeof7jmPrU+Tag==',
# }

# response = session.post('https://poliedrodist.comcel.com.co/login/catchlogon.asp', cookies=cookies, headers=headers, data=data)

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # 'Content-Length': '0',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=48DECE43CAB3B4E2780F5A56062B015AC1B7A93BEC0CA2D59BCE26536776FBD0DDF9E4A390202F3D2CB78D8B22ADA09B2B2ED5C613DA064B2BA66ADBEC15A285258BC22611729DABE341E409A97DD5A31D8681A11C0C9768B3373D884C2A4B76934A3B8F425ED642A55627703142E825BC32879F',
#     'Origin': 'https://poliedrodist.comcel.com.co',
#     'Referer': 'https://poliedrodist.comcel.com.co/login/catchlogon.asp',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# response = session.post(
#     'https://poliedrodist.comcel.com.co/Entrada.asp?A=46454656435B5C0B0006060B020004054A595C525A515851520B064F5141476E42415F420E101C0C0209070D010805660C700970600F7060700C7264660D7B0879660C7709630D64610D620C630961660F6A0D70617F094F575856574758435B5C0B61726963787D4E575F47470B77050006051804030603054D565242510E070518010B1C0404010213040B07060C0402164319115F1D&ruta_validacion_sap=/sap/web/',
#     cookies=cookies,
#     headers=headers,
# )

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'es-ES,es;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'ASPSESSIONIDSSSQABQB=FCCPMCPDCFDKHPEIJFDACMFP; dtCookie=v_4_srv_5_sn_ED8FC3D67077BAE28A816751348FC9F1_perc_100000_ol_0_mul_1_app-3Ab98757ce7cb78e31_0_rcs-3Acss_0; ASP.NET_SessionId=3mxi0huvg3muxbk3gz3yj1pu; ASPSESSIONIDSCDBCARB=JJABNCPDHMBNFNEDFKKEOJMG; Username=45085166; NSC_QpmjfespEjtusjX2l3=ffffffffaf1e1a7d45525d5f4f58455e445a4a423660; .LOGPOL=48DECE43CAB3B4E2780F5A56062B015AC1B7A93BEC0CA2D59BCE26536776FBD0DDF9E4A390202F3D2CB78D8B22ADA09B2B2ED5C613DA064B2BA66ADBEC15A285258BC22611729DABE341E409A97DD5A31D8681A11C0C9768B3373D884C2A4B76934A3B8F425ED642A55627703142E825BC32879F',
#     'Referer': 'https://poliedrodist.comcel.com.co/login/catchlogon.asp',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }

# response = session.get('https://poliedrodist.comcel.com.co/bienvenid.asp', cookies=cookies, headers=headers)

# for cookie in session.cookies:
#     if cookie.name not in cookies.keys():
#         pass
#     cookies[cookie.name] = cookie.value


# options = EdgeOptions()
# options.use_chromium = True
# options.add_argument("start-maximized")
# driver = Edge(executable_path='msedgedriver.exe', options=options)
# driver.get('https://www.example.com')
# for cookie in session.cookies:
#     driver.add_cookie({'name': cookie.name, 'value': cookie.value, 'path': '/'})
# driver.get('https://poliedrodist.comcel.com.co/bienvenid.asp')

# pass