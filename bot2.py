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
usuario = 'crpgjarvis20@gmail.com'
dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')
time.sleep(5)
############################################################
def bot():
    try:
        print('\n')
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
        print('\n')
############################################################
while True:
    bot()
    try:
#PEGAR TELEFONE
        telefone_cliente = driver.find_element(By.XPATH,contato_cliente)
        telefone_final = telefone_cliente.text 
        print(telefone_final)
        time.sleep(2)
############################################################
        #PEGAR A MENSAGEM DO CLIENTE
        todas_as_msg = driver.find_elements(By.CLASS_NAME,msg_cliente)
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg[-1] 
        print(msg)
        time.sleep(2)
############################################################
        #RESPONDENDO CLIENTE
        resposta = requests.get('http://localhost/BOT_CURSO/index.php?',params={'msg':msg,'telefone':telefone_final,'usuario':usuario},headers=agent)
        resposta = resposta.text
        time.sleep(2)
        campo_de_texto = driver.find_element(By.XPATH,caixa_msg)
        campo_de_texto.click()
        time.sleep(2)
        campo_de_texto.send_keys(resposta,Keys.ENTER)
############################################################
        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        print('AGUARDANDO NOVAS MENSAGENS')
