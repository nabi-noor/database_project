from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotVisibleException
import os
import time
from urllib.parse import quote_plus
import requests
import urllib.parse
import sys

if os.name == "nt":
    driverPath = "chrome_driver/driver/chromedriver.exe"
    dataPath = "chrome_driver/Data"
else:
    driverPath = "chrome_driver/driver/chromedriver"
    dataPath = "chrome_driver/Data/ChatBot"

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + dataPath)
driver = webdriver.Chrome(options=options, executable_path=driverPath)
driver.get('https://www.facebook.com/marketplace/auckland/vehicles')
time.sleep(10)
# for i in range (10):
#     driver.execute_script(    "window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(10)



def get_facebook_mp_data(ad):
    ad.click()
    time.sleep(10)
    element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span')
    print(element.text)
    # element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div[1]/div/span')
    # print(element.text)
    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[1]/span/span')
    print(element.text)
    # element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/span')
    # print(element.text)
    # print(driver.current_url)
    # element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/img')
    # print(element.get_attribute("src"))
    ActionChains(driver).key_down(Keys.ESCAPE).perform()

def navigate_facebook_mp():
    element = driver.find_elements_by_class_name('kbiprv82')
    for e in element:
        get_facebook_mp_data(e)
        time.sleep(10)




navigate_facebook_mp()