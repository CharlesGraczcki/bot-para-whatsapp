from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r" user-data-dir= " + dir_path + "/pasta/sessao" )
driver = webdriver.Chrome(chrome_options = chrome_options2)
driver.get("https://web.whatsapp.com/")
time.sleep(10)

time.sleep(10)

def bot():
    Try: print('oi') 

    Except: print('oi')

while True:
    bot()