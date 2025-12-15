import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

st.title("Delhi Metro Analysis")

@st.cache_data
def load_data():
    return pd.read_csv("delhi_metro_cleaned_Dataset.csv")

df = load_data()

plt.figure(figsize=(8,5))
plt.hist(df['Passengers'], bins=20, color = 'yellow', edgecolor = 'black')
plt.title('Passengers Distribution')
plt.xlabel('Passengers per Trip')
plt.ylabel('Frequency')
st.pyplot()

