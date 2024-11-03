import streamlit as st
import datetime
import time


@st.cache_data(ttl=60)  # $  cache data for 60 seconds
def fetch_data():
    time.sleep(5)
    return {"data": "Cached data"}


button = st.button("Download data")
placeholder = st.empty()

if button:
    placeholder.progress(0, "Fetching data ...")

    time.sleep(1)
    placeholder.progress(80, "Fetching data ...")
    time.sleep(1)

    data = fetch_data()
    placeholder.write(data)
