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
County=[]
Cases=[]
Deaths=[]

options = Options()
# options.add_argument('--headless')
# options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want

driver = selenium.webdriver.Chrome('D:\chromedriver', options=options)

driver.get('https://www.dhs.wisconsin.gov/covid-19/county.htm')
time.sleep(20)
tbody=driver.find_elements_by_tag_name('tbody')[0]

table=tbody.find_elements_by_tag_name('tr')
for data in table:
 County.append(data.find_elements_by_tag_name('td')[0].text)
 Cases.append(data.find_elements_by_tag_name('td')[1].text)
 Deaths.append(data.find_elements_by_tag_name('td')[3].text)

data= pd.DataFrame({
'State':'Wisconsin',
'County':County,
'New Cases': Cases,
'Deaths':Deaths,
'Date_parsing': time_of_parsing
})

data.to_csv('Wisconsin.csv')
