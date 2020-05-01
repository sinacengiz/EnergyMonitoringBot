from selenium import webdriver
from bs4 import _soup
import time
class EnergyAutomation():
    def __init__(self):
        browser = webdriver.Chrome()
        browser.get("https://osos.akdenizedas.com.tr/osos/login.iface")
        enter_user = browser.find_element_by_id("frmLoginPanel:inpUser")
        enter_pswrd = browser.find_element_by_id("frmLoginPanel:inpPass")
        enter_btn = browser.find_element_by_id("frmLoginPanel:cmdBtnValidate")
        enter_user.send_keys("sinacengiz@gmail.com")
        enter_pswrd.send_keys("maverick1")
        enter_btn.click()
        time.sleep(100)
        browser.close()
energy_aut = EnergyAutomation()
