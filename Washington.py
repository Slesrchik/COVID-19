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
Data=[]
options = Options()
options.add_argument('--headless')
# options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want
driver = selenium.webdriver.Chrome(executable_path='D:\chromedriver',
                              options=options)
driver.get('https://www.doh.wa.gov/Emergencies/Coronavirus')
time.sleep(20)
tablee=driver.find_element_by_link_text('Confirmed Cases and Deaths by County')
tablee.click()
time.sleep(3)
tbody=driver.find_element_by_id('pnlConfirmedCasesDeathsTbl')
table=tbody.find_element_by_tag_name('tbody')
tr=table.find_elements_by_tag_name('tr')[:40]
for data in tr:
 county=(data.find_elements_by_tag_name('td'))
 for c in county:
     Data.append(c.text)
data= pd.DataFrame({
'State':'Washington',
'County':Data[0::3],
'Cases': Data[1::3],
'Deaths':Data[2::3],
'Date_parsing': time_of_parsing
})
data.to_csv('D:\Washington.csv')
driver.quit()
