import selenium
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
import pandas as pd
import os
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')
County_cases=[]
Death_by_county=[]
State_cases=[]
Death_by_state=[]
County=[]
options = Options()
options.add_argument('--headless')
# options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want
driver = selenium.webdriver.Chrome('D:\chromedriver', options=options)
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=WV')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'West Virginia',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\West_Virginia.csv')
