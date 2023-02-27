import pandas as pd
import streamlit as st
import gspread

from oauth2client.service_account import ServiceAccountCredentials

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.

data = df.get_all_records()  # Get a list of all records
print(data)
