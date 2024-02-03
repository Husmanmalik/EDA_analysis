import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('PK COVID-19-10may.csv')
df1 = pd.DataFrame(df)
# Generate a profile report
st.title('EDA Analysis of Covid-19 Cases')
profile = ProfileReport(df, explorative=True)
profile.to_file("covid_19.html")
# or
profile.to_notebook_iframe()
