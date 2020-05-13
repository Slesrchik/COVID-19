import requests
import datetime
import pandas as pd
County = []
Cases = []
Deaths = []
date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
for websource in requests.get('http://dph.illinois.gov/sitefiles/COVIDHistoricalTestResults.json?nocache=1').json()[
    'characteristics_by_county']['values']:
    County.append(websource['County'])
    Cases.append(websource['confirmed_cases'])
    Deaths.append(websource['deaths'])
data = pd.DataFrame({
    'State': 'Illinois',
    'County': County,
    'Cases': Cases,
    'Deaths': Deaths,
    'Date_parsing': date_parsing
})
data.to_csv('Illinois.csv')


