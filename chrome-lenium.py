# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:47:19 2019

@author: g_osm
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\g_osm\chromedriver_win32/chromedriver')
driver.get('http://www.google.com')

q = driver.find_element(By.NAME, 'q')
q.send_keys('webdriver')
q.submit()

print(driver.title)
