import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#function to load env variables
load_dotenv()

#get a particular env variable and store in a variable
login_id = os.environ.get("LOGIN_ID")
password = os.environ.get("PASSWORD")

#connect to the chromedriver installed in the system
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)

#with the help of webdriver, open the required link
browser.get(('https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener'))

#wait until the page is loaded completely
browser.implicitly_wait(20) 

#get control of the element on the webpage using find_element() and perform the
#requied operations using the built in selenium functions

myScreenButton = browser.find_element(By.XPATH, '/html/body/main/section/div/div[1]/div/button[5]')
myScreenButton.click()
#explicit sleeps added so that the script does not crash when the webpage is loading
sleep(3)

loginRef = browser.find_element(By.XPATH, '/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[1]/input')
loginRef.send_keys(login_id) #pass login_id to the loginRef input element
passWordRef = browser.find_element(By.XPATH, '/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[2]/input')
passWordRef.send_keys(password) #pass password to the passwordRef input element

signInButton = browser.find_element(By.XPATH, '/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/button')
signInButton.click()
sleep(5)

runButton = browser.find_element(By.XPATH, '/html/body/main/section/div/div[6]/section/div/div/div/div/table/tbody/tr/td[3]/a[1]')
runButton.click()
sleep(2)

selectAllTickers = browser.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/table/thead/tr/th[1]/input')
selectAllTickers.click()
sleep(5)

csvButton = browser.find_element(By.XPATH, '/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[1]/a[1]')
csvButton.click()






