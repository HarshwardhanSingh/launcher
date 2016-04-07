import os
from datetime import datetime
from threading import Timer
from subprocess import call
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


secs = 10

def repeat():
	os.system("subl")
	driver = webdriver.Firefox()
	driver.get("http://google.com")
	time.sleep(5)
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
	driver.get('http://youtube.com/')
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
	driver.get('http://facebook.com/')
 
t = Timer(secs, repeat)
t.start()
