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
else:
    driverPath = "chrome_driver/driver/chromedriver"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, executable_path=driverPath)


def get_facebook_mp_data(ad):
    ad.click()
    time.sleep(5)
    element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/span')
    name = element.text
    element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div[1]/div/span')
    desc = element.text
    element = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[1]/span/span')
    location = element.text
    element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/span')
    price = element.text
    url = driver.current_url
    website = 'facebook.com'
    element = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/img')
    img = element.get_attribute("src")
    checkdata(name,desc,price,location,url,website,img)
    ActionChains(driver).key_down(Keys.ESCAPE).perform()

def navigate_facebook_mp():
    element = driver.find_elements_by_class_name('kbiprv82')
    for e in element:
        get_facebook_mp_data(e)
        time.sleep(5)


def get_trademe_data(ad):
    driver.get(ad)
    time.sleep(5)
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/h1')
    name = element.text
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[3]/tm-motors-listing-body/div/tg-row[1]/tg-col[2]/tm-markdown/div/p')
    desc = element.text
    try:
      element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/div/tm-motors-listing-classified/tm-motors-classified-price-box/tg-box2/div/h3')  
    except Exception:
        try:
            element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/div/tm-buy-now-box/tg-box2/div/div/p[2]/strong')  
        except Exception:
            try:
                element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[2]/tm-buyer-options/div/tm-listing-auction/tg-box2/p[2]/strong')  
            except Exception:
                return
    price = element.text
    element = driver.find_element_by_xpath('/html/body/trade-me/div[1]/main/div/tm-motors-listing/div[2]/section[3]/div/tm-listing-date-location/span[3]')
    location = element.text
    url = driver.current_url
    website = 'https://www.trademe.co.nz'
    element = driver.find_element_by_tag_name('tg-aspect-ratio')
    img = element.get_attribute("style")
    img = re.search("(?P<url>https?://[^\s]+)", img).group("url")
    checkdata(name,desc,price,location,url,website,img)


def navigate_trademe():
    element = driver.find_elements_by_class_name('tmm-sf-search-card-list-view__link')
    refList = []
    for e in element:
        e = e.get_attribute('href')
        if e not in refList:
            refList.append(e)
    for e in refList:
        get_trademe_data(e)
        time.sleep(5)
def checkdata(name,desc,price,location,url,website,img):
    params = {
        "action":"duplicate",
        "url":url
    }
    try:
        r = requests.post("https://huzoorbux.com/demoP/api/index.php", params=params)
        reply = r.json()
        if reply["reply"] is "true":
            print("Already Available")
        if reply["reply"] == "false":
            savedata(name,desc,price,location,url,website,img)
        else:
            return False
    except Exception:
        print("server ERROR!!")

def savedata(name,desc,price,location,url,website,pic):
    params = {
        "action":"insert",
        "name":name,
        "desc":desc,
        "price":price,
        "location":location,
        "pic":pic,
        "url":url,
        "website":website,
    }
    try:
        r = requests.post("https://huzoorbux.com/demoP/api/index.php", params=params)
        reply = r.json()
        print(reply["reply"])
    except Exception:
        print("server ERROR!!")

url = input("Enter the link that you want to scrape\n")

if("facebook.com" in url):
    driver.get(url)
    time.sleep(5)
    for i in range (10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
    navigate_facebook_mp()
elif ("trademe.co.nz" in url):
    driver.get(url)
    time.sleep(10)
    for i in range (10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
    navigate_trademe()
else:
    print("We do not support the website that you want to crawl")