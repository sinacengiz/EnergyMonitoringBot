
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import time
#import jenkins tools

class EnergyAutomation():
    def __init__(self):
        self.automate()
        self.get_data()
    def automate(self):
        browser = webdriver.Chrome("C:/Users/User/Desktop/chromedriver.exe")
        browser.get("https://osos.akdenizedas.com.tr/osos/login.iface")
        browser.maximize_window()
        enter_user = browser.find_element_by_id("frmLoginPanel:inpUser")
        enter_pswrd = browser.find_element_by_id("frmLoginPanel:inpPass")
        enter_btn = browser.find_element_by_id("frmLoginPanel:cmdBtnValidate")
        enter_user.send_keys("2687521000")
        enter_pswrd.send_keys("Aa.010420")
        enter_btn.click()
        time.sleep(15)
        click_btn=browser.find_element_by_id("frmCounters:counterList:0:j_id101-0-0")
        click_btn.click()
        startdate=browser.find_element_by_name("ffrmCounterProfilestxtStartDate1")
        startdate.click()
        time.sleep(1000)
    def get_data(self):
        self.page=requestgits.get(browser.current_url)
        soup=BeautifulSoup(self.page.content,"html.parser")
        data = soup.find_all("table", {"class": "chart full-width"})
        browser.close()
    def graph(self):
        pass
    def notify(self):
        pass

    
energy_aut = EnergyAutomation()
