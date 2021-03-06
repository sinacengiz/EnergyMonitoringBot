from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
#import jenkins tools

class EnergyAutomation():
    def __init__(self):
        self.automate()
        self.get_data()
    def automate(self):
        browser = webdriver.Chrome()
        browser.get("https://osos.akdenizedas.com.tr/osos/login.iface")
        enter_user = browser.find_element_by_id("frmLoginPanel:inpUser")
        enter_pswrd = browser.find_element_by_id("frmLoginPanel:inpPass")
        enter_btn = browser.find_element_by_id("frmLoginPanel:cmdBtnValidate")
        enter_user.send_keys("sinacengiz@gmail.com")
        enter_pswrd.send_keys("maverick1")
        enter_btn.click()
        time.sleep(100)
    def get_data(self):
        page=requests.get(browser.current_url)
        soup=BeautifulSoup(page.content,"html.parser")
        data = soup.find_all("table", {"class": "chart full-width"})
        browser.close()
    def graph(self):
        pass
    def notify(self):
        pass
    #use whatsapp API to notify
    
energy_aut = EnergyAutomation()
