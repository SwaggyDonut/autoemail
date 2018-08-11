# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:18:14 2018

@author: SwaggyDonut
Gmail test
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

subject_text = 'test title'
message = 'test title'

def add_driver():
    driver = webdriver.Chrome("C:/Users/zhang/Desktop/chromedriver_win32/chromedriver.exe")
    return driver

#set up webdriver to direct to the server
def get_url(driver):
    driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

def login(driver):
    driver.find_element_by_name("identifier").send_keys('duona.test@gmail.com')
    driver.find_element_by_xpath("//*[@id = 'identifierNext']/content/span").click()
    driver.implicitly_wait(4)
    driver.find_element_by_name("password").send_keys('duonatest')
    driver.find_element_by_xpath("//*[@id = 'passwordNext']/content/span").click()

def subject_text(driver):
    composeElem = driver.find_element_by_class_name('z0')
    composeElem.click()

    toElem = driver.find_element_by_name("to")
    toElem.send_keys('zhangduona1995@gmail.com')

    subjElem = driver.find_element_by_name("subjectbox")
    subjElem.send_keys(subject_text)

    editable = driver.find_element_by_css_selector('.editable')
    if editable:
        editable.click()
        editable.send_keys(message)

def send_email(driver):
    try:
        send = driver.find_elements_by_xpath('//div[@role="button"]')
        for s in send:
            if s.text.strip() == 'Send':
                s.click()
    except:
        pass

<<<<<<< HEAD

=======
>>>>>>> b1
def quit(driver):
    driver.quit()		

def main():
    driver = add_driver()
    get_url(driver)
    login(driver)
    subject_text(driver)
    send_email(driver)
    quit(driver)  		

if __name__ == '__main__':
    main()		
<<<<<<< HEAD


=======
>>>>>>> b1

