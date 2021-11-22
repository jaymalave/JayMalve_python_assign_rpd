import os
import csv
import pandas as pd
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
load_dotenv()


chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)

browser.get(('https://www.zacks.com/funds/etf/veu/holding'))

df = pd.read_csv('data.csv')

ticker_list = df.iloc[:, 0].to_list()

print(ticker_list)

for ticker in ticker_list:
    browser.refresh()
    sleep(20)
    searchRef = browser.find_element_by_css_selector('#ticker')
    searchRef.send_keys(ticker.upper())
    searchRef.submit()
    sleep(3)

    table = browser.find_element_by_css_selector("#etf_holding_table")
    with open(ticker + '.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in table.find_elements_by_css_selector('tr'):
            wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
    


