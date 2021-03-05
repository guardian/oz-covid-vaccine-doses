import requests
import pandas as pd  
import os

data_path = os.path.dirname(__file__) + "/data/"

df = pd.read_html("https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/getting-vaccinated-for-covid-19/how-covid-19-vaccines-will-be-distributed")

print(df)