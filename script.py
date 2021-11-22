import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()


login_id = os.environ.get("LOGIN_ID")
password = os.environ.get("PASSWORD")

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)


browser.get('https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener')

browser.maximize_window() # For maximizing window
browser.implicitly_wait(20) # gives an implicit wait for 20 seconds

myScreenButton = browser.find_element_by_xpath('/html/body/main/section/div/div[1]/div/button[5]')
myScreenButton.click()
sleep(3)

loginRef = browser.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[1]/input')
loginRef.send_keys(login_id)
passWordRef = browser.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[2]/input')
passWordRef.send_keys(password)

signInButton = browser.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/button')
signInButton.click()
sleep(5)

runButton = browser.find_element_by_xpath('/html/body/main/section/div/div[6]/section/div/div/div/div/table/tbody/tr/td[3]/a[1]')
runButton.click()
sleep(2)

selectAllTickers = browser.find_element_by_xpath('/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/table/thead/tr/th[1]/input')
selectAllTickers.click()
sleep(2)

csvButton = browser.find_element_by_xpath('/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[1]/a[1]')
csvButton.click()


print("done")





