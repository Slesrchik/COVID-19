#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=IL')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Illinois',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Illinois.csv')


# In[24]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=IN')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Indiana',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Indiana.csv')


# In[25]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=IA')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Iowa',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Iowa.csv')


# In[26]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=KS')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Kansas',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Kansas.csv')


# In[39]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=LA')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Louisiana',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Louisiana.csv')


# In[29]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=ME')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Maine',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Maine.csv')


# In[40]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=MD')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Maryland',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Maryland.csv')


# In[31]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=VT')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Vermont',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Vermont.csv')


# In[32]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=WA')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Washington',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Washington.csv')


# In[33]:


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


# In[34]:


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
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/county-map.html?state=WI')
time.sleep(5)
# table=driver.find_element_by_class_name('allborders rowbackgrounds')
tbody=driver.find_element_by_tag_name('tbody')
tr=tbody.find_elements_by_tag_name('tr')
for i in tr:
    County.append(i.find_elements_by_tag_name('td')[0].text)
    County_cases.append((i.find_elements_by_tag_name('td')[1].text))
    Death_by_county.append((i.find_elements_by_tag_name('td')[3].text))
data= pd.DataFrame({
    'State':'Wisconsin',
    'County':County,
    'Cases': County_cases,
    'Deaths':Death_by_county,
    'Date_parsing': time_of_parsing
})
data.to_csv('D:\Wisconsin.csv')


# In[ ]:




