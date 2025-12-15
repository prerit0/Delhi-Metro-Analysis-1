import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Delhi Metro Analysis",
    layout="wide"
)

st.title("🚇 Delhi Metro Analysis Dashboard")
st.markdown(
    "An exploratory data analysis of Delhi Metro passenger trends, stations, and ticket usage."
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("delhi_metro_cleaned_Dataset.csv")

df = load_data()

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------
st.header("📄 Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Total Stations", df['From_Station'].nunique())
col3.metric("Ticket Types", df['Ticket_Type'].nunique())

st.subheader("Sample Data")
st.dataframe(df.head())

# --------------------------------------------------
# Passenger Distribution
# --------------------------------------------------
st.header("👥 Passenger Distribution")

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.hist(df['Passengers'], bins=20, edgecolor='black')
ax1.set_title("Passengers Distribution")
ax1.set_xlabel("Passengers per Trip")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# --------------------------------------------------
# Top Stations Analysis
# --------------------------------------------------
st.header("🚉 Top 10 Busy Stations")

station_counts = (
    df['From_Station']
    .value_counts()
    .nlargest(10)
)

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.barh(station_counts.index, station_counts.values)
ax2.invert_yaxis()
ax2.set_xlabel("Number of Trips")
ax2.set_title("Top 10 From Stations")
st.pyplot(fig2)

# --------------------------------------------------
# Ticket Type Analysis
# --------------------------------------------------
st.header("🎟️ Ticket Type Distribution")

ticket_counts = df['Ticket_Type'].value_counts()

fig3, ax3 = plt.subplots(figsize=(6, 4))
ax3.bar(ticket_counts.index, ticket_counts.values)
ax3.set_xlabel("Ticket Type")
ax3.set_ylabel("Count")
ax3.set_title("Ticket Type Usage")
st.pyplot(fig3)

# --------------------------------------------------
# Peak Hour Analysis (if column exists)
# --------------------------------------------------
if 'Hour' in df.columns:
    st.header("⏰ Peak Hour Analysis")

    hour_counts = df['Hour'].value_counts().sort_index()

    fig4, ax4 = plt.subplots(figsize=(8, 4))
    ax4.plot(hour_counts.index, hour_counts.values, marker='o')
    ax4.set_xlabel("Hour of Day")
    ax4.set_ylabel("Trips")
    ax4.set_title("Trips by Hour")
    st.pyplot(fig4)

# --------------------------------------------------
# Key Insights
# --------------------------------------------------
st.header("📌 Key Insights")

st.markdown("""
- Passenger counts show a **right-skewed distribution**, indicating peak crowding at certain times.
- A small number of stations handle **majority of the traffic**.
- **Ticket usage patterns** suggest commuter preference trends.
- Peak-hour trends highlight **rush hours** in the metro network.
""")

st.markdown("---")
st.caption("📊 Built with Streamlit | Data Source: Delhi Metro Dataset")
