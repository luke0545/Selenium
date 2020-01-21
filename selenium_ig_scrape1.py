from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

#launch url
url = "https://www.instagram.com/therock/"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

followers = driver.find_element_by_xpath("""/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span""")
print(followers.text)

jumunji_link = driver.find_element_by_xpath("""/html/body/div[1]/section/main/div/header/section/div[2]/a[1]""").click()

#posts = driver.find_element_by_class_name("g47SY ")
#python_button.click() #click fhsu link
#driver.find_element_by_