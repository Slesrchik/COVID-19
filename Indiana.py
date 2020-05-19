import requests
import datetime
import pandas as pd
import csv
import codecs
req = requests.get('https://hub.mph.in.gov/dataset/89cfa2e3-3319-4d31-a60d-710f76856588/resource/8b8e6cd7-ede2-4c41-a9bd-4266df783145/download/covid_report_county.xlsx')
url_content = req.content
csv_file = open('D:\Indiana.csv', 'wb')

csv_file.write(url_content)
csv_file.close()
