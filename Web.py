import time

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
browser = Firefox(options=opts)
from selenium.webdriver.support.select import Select

driver = Firefox()

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

browser.get("https://www.adapt.io/login.htm?slc=web&login=true")
element = browser.find_element_by_name("emailSignIn")
element.send_keys("rathiishan@yahoo.com")
time.sleep(1)
element = browser.find_element_by_name("passwordSignin")
element.send_keys("ishan2000")
element = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div/data-signup/div/div[2]/div[1]/form/div[3]/div[1]/button")
element.click()
time.sleep(5)
element = browser.find_element_by_xpath("/html/body/div[1]/div[2]/section/main/div/div[1]/div/div[4]/button")
element.click()
time.sleep(2)
element = browser.find_element_by_id("company-tab-id")
element.click()
time.sleep(2)
element = browser.find_element_by_id("locationcompanypage")
element.send_keys(input("Please enter the state: "))
time.sleep(3)
state = Select(element.find_element_by_class_name("suggestion-mask"))
state.select_by_index(0)
element = browser.find_element_by_xpath("/html/body/div[1]/div[2]/section/main/div/div[1]/div[2]/div/div[3]/div/div[1]/svg")
element.click()
element.find_element_by_name("ALL")
element.click()
element.find_element_by_name("Energy & Utilities")
element.click()


