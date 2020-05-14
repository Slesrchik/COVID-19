import pandas as pd
d = pd.read_html ("https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml")
df = d[2]
df.to_csv('Maine.csv')
