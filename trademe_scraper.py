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
import re



if os.name == "nt":
    driverPath = "chrome_driver/driver/chromedriver.exe"
    dataPath = "chrome_driver/Data"
else:
    driverPath = "chrome_driver/driver/chromedriver"
    dataPath = "chrome_driver/Data/ChatBot"

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + dataPath)
driver = webdriver.Chrome(options=options, executable_path=driverPath)
driver.get('https://www.trademe.co.nz/motors/used-cars')
time.sleep(20)


# for i in range (10):
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(10)



def get_trademe_data(ad):
    driver.get(ad)
    time.sleep(20)
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/h1')
    print(element.text)
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/div/tm-motors-listing-classified/tm-motors-classified-price-box/tg-box2/div/h3')
    print(element.text)
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[3]/tm-motors-listing-body/div/tg-row[1]/tg-col[2]/tm-markdown/div')
    print(element.text)
    print(driver.current_url)
    element = driver.find_element_by_tag_name('tg-aspect-ratio')
    img = element.get_attribute("style")
    print(re.search("(?P<url>https?://[^\s]+)", img).group("url"))

def navigate_trademe():
    element = driver.find_elements_by_class_name('tmm-sf-search-card-list-view__link')
    refList = []
    for e in element:
        refList.append(e.get_attribute('href'))
    for e in refList:
        get_trademe_data(e)
        time.sleep(20)




navigate_trademe()

