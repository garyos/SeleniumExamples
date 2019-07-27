# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 11:05:37 2019

@author: g_osm
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new chrome session (path added manually to save restart)
driver = webdriver.Chrome(r'C:\Users\g_osm\chromedriver_win32/chromedriver')


#geckodriver needed to be added to path in order for this to work
#driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_name('q')

search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("LC20lb")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()