import requests
import datetime
import pandas as pd
Dictionary = []
County = []
Cases = []
Deaths = []
date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
for websource in requests.get('https://services5.arcgis.com/O5K6bb5dZVZcTo5M/arcgis/rest/services/Cases_by_Parish/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=LDHH%2CParish%2CCases%2CDeaths%2CCommercial_Tests%2CState_Tests%2CFID%2CColumn10%2CColumn11&orderByFields=FID%20ASC&outSR=102100').json()[
    'features']:
    Dictionary.append(websource['attributes'])
for web in Dictionary:
    County.append(web['Parish'])
    Cases.append(web['Cases'])
    Deaths.append(web['Deaths'])
data = pd.DataFrame({
    'State': 'Louisana',
    'County': County,
    'Cases':  Cases,
    'Deaths': Deaths,
    'Date_parsing': date_parsing
})
data.to_csv('Louisana.csv')
