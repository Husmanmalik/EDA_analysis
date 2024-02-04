import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('data_set1.csv')
df1 = pd.DataFrame(df)
# Generate a profile report
st.title('EDA Analysis of Covid-19 Cases')
profile = ProfileReport(df, explorative=True)
st_profile_report(profile)

