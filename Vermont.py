import selenium #доделать
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
# import data
# import xlrd
import pandas as pd
import os
import datetime
time_of_parsing=datetime.datetime.today().strftime('%Y-%m-%d')
Data=[]
County=[]
Cases=[]
Deaths=[]
options = Options()
options.add_argument('--headless')
# options.add_argument("download.default_directory=/Users/giova/Documents/Data Mining/COVID-19")#change path what you want
driver = webdriver.Chrome(executable_path='D:\chromedriver',
                                  options=options)
driver.get('https://vcgi.maps.arcgis.com/apps/opsdashboard/index.html#/6128a0bc9ae14e98a686b635001ef7a7')
time.sleep(20)
tbody=driver.find_elements_by_class_name('feature-list')[0]
table=tbody.find_elements_by_tag_name('p')
for data in table:
    County.append(data.find_elements_by_tag_name('strong')[0].text)
data= pd.DataFrame({
'State':'Vermont',
'County':County[0::5],
'Cases': County[1::5],
'Deaths':County[3::5],
'Date_parsing': time_of_parsing
})
data.to_csv('Vermont.csv')
