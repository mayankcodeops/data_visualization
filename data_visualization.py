import requests
import pandas as pd

COVID_DISTRICT_WISE_URL = 'https://data.covid19india.org/state_district_wise.json'
COVID_STATE_WISE_DAILY_URL = 'https://api.covid19india.org/states_daily.json'

# fetching JSON data for state wise daily reports
state_wise_json = requests.get(COVID_STATE_WISE_DAILY_URL)

# Converting to a dictionary for data cleaning
covid_data = state_wise_json.json()
covid_data = covid_data['states_daily']
# normalize json
covid_data = pd.json_normalize(covid_data)
print(covid_data)

