################################################ Citi BIKES DASHBOARD #####################################################

import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt

########################### Initial settings for the dashboard ##################################################################


st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")
st.markdown("The dashboard will help with the expansion problems Citi Bike currently faces")
st.markdown("Right now, Citi bikes runs into a situation where customers complain about bikes not being available at certain times. This analysis aims to look at the potential reasons behind this.")

########################## Import data ###########################################################################################

df = pd.read_csv('daily_rides_vs_temperature.csv', index_col = 0)
top_20 = pd.read_csv('top_20.csv', index_col = 0)

# ######################################### DEFINE THE CHARTS #####################################################################

## Bar chart

fig = go.Figure(go.Bar(x = top_20['start_station_name'], y = top_20['value'], marker={'color': top_20['value'],'colorscale': 'Blues'}))
fig.update_layout(
    title = 'Top 20 most popular bike stations in New York',
    xaxis_title = 'Start stations',
    yaxis_title ='Sum of trips',
    width = 900, height = 600
)
st.plotly_chart(fig, use_container_width=True)


## Line chart 

fig_2 = make_subplots(specs = [[{"secondary_y": True}]])

fig_2.add_trace(
go.Scatter(x = df['date'], y = df['bike_rides_daily'], name = 'Daily bike rides', marker={'color': df['bike_rides_daily'],'color': 'blue'}),
secondary_y = False
)

fig_2.add_trace(
go.Scatter(x=df['date'], y = df['avgTemp'], name = 'Daily temperature', marker={'color': df['avgTemp'],'color': 'red'}),
secondary_y=True
)

fig_2.update_layout(
    title = 'Daily bike trips and temperatures in 2022',
    height = 600
)

st.plotly_chart(fig_2, use_container_width=True)


### Add the map ###

path_to_html = "Citi_bike Trips Aggregated.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Aggregated Bike Trips in New York")
st.components.v1.html(html_data,height=1000)
