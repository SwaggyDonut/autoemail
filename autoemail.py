# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:18:14 2018

@author: zhang
"""

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random


driver = webdriver.Chrome("C:/Users/zhang/Desktop/chromedriver_win32/chromedriver")
#set up webdriver to direct to the server
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_name("identifier").send_keys('duona.test@gmail.com')
driver.find_element_by_xpath("//*[@id = 'identifierNext']/content/span").click()
driver.implicitly_wait(4)
driver.find_element_by_name("password").send_keys('duonatest')
driver.find_element_by_xpath("//*[@id = 'passwordNext']/content/span").click()
composeElem = driver.find_element_by_class_name('z0') #this only works half of the time
composeElem.click()

toElem = driver.find_element_by_name("to")
toElem.send_keys('zhangduona1995@gmail.com')

subjElem = driver.find_element_by_name("subjectbox")
subjElem.send_keys('Hello')

sendElem = driver.find_element_by_xpath("//div[text()='Send']")
sendElem.click()
