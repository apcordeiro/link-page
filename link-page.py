import streamlit as st
import pandas as pd
from pyreadr import read_r
import requests

response = requests.get("http://127.0.0.1:8000/dataframe/")
response.raise_for_status()
data = response.json()

if "data" in data:
    df = pd.DataFrame(data["data"], columns=data["columns"])
else:
    st.write("No data available")

print(df)
query_params = st.query_params

if query_params=={}:
    filtered_df = None
    st.text('No data found')
else:
    id = query_params['id']
    filtered_df = df[df['Id'] == id]
    if filtered_df.empty:
        st.text('No data found')
    else:
        st.title('Links')
        for index, row in filtered_df.iterrows():
            title = row['Title']
            link = row['Link']
            # Display the title as a clickable link
            st.markdown(f'[{title}]({link})')
