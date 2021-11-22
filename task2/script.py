import csv
import pandas as pd
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#function to load env variables
load_dotenv()


#connect to the chromedriver installed in the system
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)


#with the help of webdriver, open the required link
browser.get(('https://www.zacks.com/funds/etf/veu/holding'))


#read the csv file(in the same directory) using read_csv() function in pandas
df = pd.read_csv('data.csv')


#access the first column in the csv file and save the elements in the column in a list
ticker_list = df.iloc[:, 0].to_list()


#traverse through every ticker in the list and perform the required scraping operation
for ticker in ticker_list:
    browser.refresh() #refresh the page after every ticker scraping operation
    sleep(20)

    #get control of the element on the webpage using find_element() and perform the
    #requied operations using the built in selenium functions

    searchRef = browser.find_element(By.CSS_SELECTOR, '#ticker') 
    #transform ticker into all uppercase and pass as an input to searchRef
    searchRef.send_keys(ticker.upper()) 
    searchRef.submit()  #selenium function to press enter
    sleep(3)
  

    #get access to the table
    table = browser.find_element(By.CSS_SELECTOR, "#etf_holding_table")
    #create a new csv file named after the corresponding ticker and write to it
    
    with open(ticker + '.csv', 'w', newline='') as csvfile:
        #use writer() from 'csv' to write to the file
        wr = csv.writer(csvfile)
        for row in table.find_elements(By.CSS_SELECTOR, 'tr'):
            #writerow() writes new rows of scraped data to the file 
            wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
    


