import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Wildfire Weather Dashboard", layout="wide")

#  Load Data
df_fwi = pd.read_csv("data/fwi_calculations/fwi_results.csv")

#  Convert time column to datetime
df_fwi["time"] = pd.to_datetime(df_fwi["time"])

#  Sidebar Filters
st.sidebar.image("assets/4.png", width=150)
st.sidebar.header("🔥 Wildfire Risk Dashboard")
date_filter = st.sidebar.date_input("Select Date", df_fwi["time"].min())

#  Filter by date
df_fwi_filtered = df_fwi[df_fwi["time"].dt.date >= date_filter]

#  Layout
st.title("🔥 Wildfire Weather Dashboard")

col1, col2 = st.columns([2, 1])

with col1:
    fig1 = px.line(df_fwi_filtered, x="time", y=["Temperature (°C)", "Wind Speed (km/h)"],
                   title="Temperature & Wind Speed Over Time",
                   labels={"WWD": "Wildfire Weather"})
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(df_fwi_filtered, x="Humidity (%)", y="Precipitation (mm)",
                      title="Humidity vs Precipitation")
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.metric(label=" Avg Fire Weather Index", value=round(df_fwi_filtered["FWI"].mean(), 2))
    st.success(" Data updates in real-time!")

st.info("💡 This dashboard integrates **real-time analytics** for wildfire risk monitoring.")

st.markdown("###  Power BI Wildfire Analysis")

POWER_BI_EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=fbf4f7e4-cf7d-4048-9da4-dc5fa55e4de0&autoAuth=true&ctid=244e6ed2-339a-47f3-b95c-e45351c198b7"

st.markdown(
    f'<iframe width="1000" height="600" src="{POWER_BI_EMBED_URL}" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True
)

st.success(" This dashboard integrates real-time updates from Streamlit with rich analytics from Power BI!")