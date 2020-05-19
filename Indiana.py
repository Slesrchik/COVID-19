import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
import xlrd
import pandas as pd
import os
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')
#print(time_of_parsing)
options = Options()
options.add_argument('--headless')                  #C:\Users\AdmiN\COVID
options.add_argument("download.default_directory=C:/Users/AdmiN/Documents/COVID") 
driver = selenium.webdriver.Chrome('D:\chromedriver', options=options)
driver.get('https://hub.mph.in.gov/dataset/89cfa2e3-3319-4d31-a60d-710f76856588/resource/8b8e6cd7-ede2-4c41-a9bd-4266df783145/download/covid_report_county.xlsx')
time.sleep(5)
df = pd.read_excel('C:/Users/AdmiN/Documents/COVID/covid_report_county.xlsx')
df.insert(1,'State','Indiana')
df.insert(5,'Date',time_of_parsing)
df.to_csv('D:\Indiana.csv')
os.remove('C:/Users/AdmiN/Documents/COVID/covid_report_county.xlsx')
