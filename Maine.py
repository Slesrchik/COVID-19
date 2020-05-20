import pandas as pd
import datetime
date_parsing = datetime.datetime.today().strftime('%Y-%m-%d')
d = pd.read_html ("https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml")
df = d[2]
df.insert(1,'State','Maine')
df.insert(6,'Date',date_parsing)
data = df[['State','Cumulative COVID‑19 Case Counts by County', 'Cumulative COVID‑19 Case Counts by County.1', 'Cumulative COVID‑19 Case Counts by County.4', 'Date']]
data.to_csv('D:\Maine.csv')
