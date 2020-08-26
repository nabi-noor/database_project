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

# chromedriver_path = os.path.join(sys._MEIPASS, driverPath)

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + dataPath)
driver = webdriver.Chrome(options=options, executable_path=driverPath)
# driver.get('http://localhost/d/d.html')
driver.get('https://web.whatsapp.com')
print('Please Scan the QR Code and press enter after complete loading.......')
input()


unread_messageClass = '_31gEB' #OUeyt
user_numberClass    = '_3ko75' #_1wjpf
send_messageClass   = '_3uMse' #_1Plpp
send_message_innerClass = '_3FRCZ' #_2S1VP
defaultName         = '935370'
process             = 1
sCounter            = 0
url                 = 'https://kingsmedicalcenter.ae/bot/api/index.php' #live server
# url                 = 'http://localhost/zohair/api/index.php' #localhost


def send_message(msg):
    whatsapp_msg_outer = driver.find_element_by_class_name(send_messageClass)
    whatsapp_msg = whatsapp_msg_outer.find_element_by_class_name(send_message_innerClass)

    for part in msg.split('\n'):
        whatsapp_msg.send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    time.sleep(1)    
    ActionChains(driver).send_keys(Keys.RETURN).perform()
    time.sleep(1)
    archiveMessage()

def archiveMessage():
    ActionChains(driver).key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("e").key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    moveDefault() # back to some default chat to avoid unread messages
    time.sleep(2)

def markUnread():
    ActionChains(driver).key_down(Keys.ALT).key_down(Keys.CONTROL).send_keys("U").key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
    time.sleep(1)
    moveDefault() # back to some default chat to avoid unread messages
    time.sleep(1)



def unreadMessageProcess():
    global process
    process = 2
    try:
        unread_chat = driver.find_element_by_class_name(unread_messageClass)
        unread_chat = unread_chat.find_element_by_xpath('./../../../../../../..')
        
        number = unread_chat.find_element_by_class_name(user_numberClass).text.replace(" ","")
        unread_chat.click()
        time.sleep(1)
        lastMessage = readLastMessage()
        if lastMessage != False:
            process = 3
            checkCommand(lastMessage,number)
        else:
            pass
        
    except Exception:
        return False

def checkCommand(command,number):
    global process
    params = {
        "action":"update",
        "command":command,
        "number":number
    }
    try:
        print(command + " <==Command received")
        r = requests.post(url, params=params)
        if r.status_code == 200:
            reply = r.json()
            if reply["reply"] != "null":
                print("sending message to==> "+number)
                send_message(reply["reply"])
                process = 1
                print("message sent")
                return False
            else:
                archiveMessage()
                process = 1
                return False
    except Exception:
        print("server ERROR!!")
        process = 1
        markUnread()
        time.sleep(20)
        return False

def readLastMessage():
    text_bubbles = driver.find_elements_by_class_name("message-in")  # message-in = receiver, message-out = sender
    tmp_queue = []

    try:
        for bubble in text_bubbles:
            msg_texts = bubble.find_elements_by_class_name("selectable-text")
            
            for msg in msg_texts:
                tmp_queue.append(msg.text.lower())

        # if len(tmp_queue) > 0:
        #     messages = ' '.join(tmp_queue) 
        #     return messages # Send messages message in list

        if len(tmp_queue) > 0:
            return tmp_queue[-1]  # Send last message in list only

    except StaleElementReferenceException as e:
        print(str(e))
    return False

def allAppointments():
    params = {
        "action":"new_messages"
    }
    try:
        r = requests.post(url, params=params)
        if r.status_code == 200:
            appointments = r.json()
            if appointments["appointments"] != 'null':
                return appointments
            else:
                return False
        else:
            return False
            
    except Exception:
        return False

def appointmentUpdate(id,status):
    params = {
        "action":"message_sent",
        "id":id,
        "status":status
    }
    try:
        requests.post(url, params=params)
        return False
    except Exception:
        return False

# def appointmentMessageSend(id,phone_no,message):
#     global process
#     process = 3
#     print( f"Sending message on: {phone_no}")
#     try:
#         driver.get( f"https://web.whatsapp.com/send?phone=${phone_no}&text="+urllib.parse.quote_plus(message) )

#         try:
#             alert = driver.switch_to.alert
#             alert.accept()
#         except Exception:
#             pass
        
#         time.sleep(7)
#         send_message = driver.find_element_by_xpath("//span[@data-icon='send']")
#         send_message.click()
#         time.sleep(1)
#         archiveMessage()
#         print( f"Message sent on: {phone_no}")
#         if id != "null":
#             appointmentUpdate(id,2)
#             process = 1
        
#     except Exception:
#         invalid_message = driver.find_element_by_xpath("//div[@role='button']")
#         invalid_message.click()
#         print("invailid phone no :"+str(phone_no))
#         appointmentUpdate(id,6)
#         process = 1

def appointmentMessageSend(id,phone_no,message):
    global process
    process = 3
    print( f"Sending message on: {phone_no}")
    phone_no = phone_no.replace("+","")
    urll = "https://wa.me/"+phone_no+"?text="+urllib.parse.quote_plus(message)
    try:
        # add new message link
        driver.execute_script("var container = document.getElementById('side'); var para = document.createElement('div'); container.insertBefore(para, container.firstChild); para.innerHTML = \"<a style='display:none;' id='interedLink' href='"+urll+"' target='_blank' rel='noopener noreferrer' class='interedLink _F7Vk selectable-text invisible-space copyable-text'>New Message</a>\";  container.insertBefore(para, container.firstChild);")
        
        time.sleep(2)
        
        # click link
        driver.execute_script("document.getElementById(\"interedLink\").click();")
        
        time.sleep(2)

        # Delete element
        driver.execute_script("var delel = document.getElementById(\"interedLink\"); delel.parentNode.parentNode.removeChild(delel.parentNode);")

        send_message = driver.find_element_by_xpath("//span[@data-icon='send']")
        send_message.click()
        time.sleep(3)
        archiveMessage()
        print( f"Message sent on: {phone_no}")
        appointmentUpdate(id,2)
        process = 1
    except Exception:
        invalid_message = driver.find_element_by_xpath("//div[@role='button']")
        invalid_message.click()
        print("invailid phone no :"+str(phone_no))
        appointmentUpdate(id,6)
        process = 1
        pass

def moveDefault():
    search = driver.find_element_by_class_name("_3FRCZ ")
    search.send_keys(defaultName+"\n")
    
    #search.send_keys(defaultName)
    #time.sleep(2)
    #ActionChains(driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()
    #ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    # time.sleep(2)
    #ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()


moveDefault()

while True:
    try:
        if process == 4:
            appointments = allAppointments()
            print("Server Check")
            if appointments != False:
                print("Messages Received in Server Check")
                for appointment in appointments['appointments']:
                    appointmentMessageSend(appointment['id'],appointment['number'],appointment['message'])
                    time.sleep(2)
            else:
                process = 1
                print("Server Check No Message")

        elif process == 1:
            print("Unread Message Check 1")
            unreadMessageProcess()

        elif process == 2:
            time.sleep(5)
            print("Unread Message Check 2")
            unreadMessageProcess()
            sCounter += 1
            if sCounter == 12:
                sCounter = 0
                process = 4
    except Exception:
        print("error....")
        pass