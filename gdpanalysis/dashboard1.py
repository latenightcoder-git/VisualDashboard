import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')
st.markdown('**GAPMINDER DASHBOARD**')
df = pd.read_csv('../datasets/gapminder_data_graphs.csv')
st.dataframe(df)
