from pandas.core.algorithms import value_counts
import requests
import pandas as pd
import matplotlib.pyplot as plt


COVID_DISTRICT_WISE_URL = 'https://data.covid19india.org/state_district_wise.json'
COVID_STATE_WISE_DAILY_URL = 'https://api.covid19india.org/states_daily.json'

# fetching JSON data for state wise daily reports
state_wise_json = requests.get(COVID_STATE_WISE_DAILY_URL)

# Converting to a dictionary for data cleaning
covid_data = state_wise_json.json()
covid_data = covid_data['states_daily']
# normalize json
covid_data = pd.json_normalize(covid_data)

#making data usable
df = covid_data

df['date'] = pd.to_datetime(df.date)
df['dateymd'] = pd.to_datetime(df.dateymd)

#taking only the confirmed cases Series records
df = df[df.status == 'Confirmed']

#removing the status column as now all the records are confirmed only
df.drop('status', axis=1, inplace=True)

#setting the date to be the index column
df.set_index('date', inplace = True)

#converting datatype to integer
df = df.apply(pd.to_numeric)

# Tabulation styling 
df = df.tail(50)

# Plotting Histogram