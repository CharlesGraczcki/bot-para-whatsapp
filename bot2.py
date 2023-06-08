from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests
############################################################
#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
#CHAVE    sIXNwyBlL4WXqeEm1o6l1XSLb1VA4ZyR
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/sIXNwyBlL4WXqeEm1o6l1XSLb1VA4ZyR" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()
############################################################
dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')
time.sleep(30)
############################################################
def bot():
    try:
        print('joguei no')
        #l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt
        bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
        bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
    except:
        print('vasco')
############################################################
while True:
    bot()
#pegar o telefone
    telefone_cliente = driver.find_element(By.XPATH,contato_cliente)
    telefonefinal = telefone_cliente.text
    print(telefonefinal)

    #PEGAR A MENSAGEM DO CLIENTE
    #todas_as_msg =driver.find_elements(By,CLASS_NAME,'')

