import streamlit as st
import pandas as pd
st.title("Data Load Test")

df = pd.read_csv("delhi_metro_cleaned_Dataset.csv")
st.dataframe(df.head())

