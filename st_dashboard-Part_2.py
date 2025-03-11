################################################ Citi BIKES DASHBOARD #######################################################

import streamlit as st
import pandas as pd
import numpy as np
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from datetime import datetime as dt
from decimal import Decimal
from numerize.numerize import numerize
from PIL import Image
########################### Initial settings for the dashboard ##############################################################


st.set_page_config(page_title = 'Citi Bikes Strategy Dashboard', layout='wide')
st.title("Citi Bikes Strategy Dashboard")

page = st.sidebar.selectbox('Aspect Selector',
    ["Intro page", "Weather component and bike usage", "Most popular stations", "Interactive map with aggregated bike trips", "Recommendations"])

########################## Import data#######################################################################################

# Load datasets

df = pd.read_csv('reduced_data_to_plot_7.csv') 
top_20 = pd.read_csv('top_20.csv', index_col = 0) 

# sort df
df.sort_values(by="date", inplace=True)

####################### DEFINE THE PAGES #########################################################################

### Intro page

if page == "Intro page":
    st.markdown("#### This dashboard aims at providing helpful insights on the expansion problems Citi Bikes currently faces.")
    st.markdown("Currently, Citi Bike faces challenges with customers reporting bike unavailability at certain times. This analysis aims to address these expansion issues by providing insights into the underlying causes and explores potential factors contributing to the problem. The dashboard is divided into four sections:")

    st.markdown("- Weather component and bike usage")
    st.markdown("- Most popular stations")
    st.markdown(" - Interactive map with aggregated bike trips")
    st.markdown(" - Recommendations")
    st.markdown(" - The dropdown menu on the left 'Aspect Selector' will take you to the different aspects of the analysis out team looked at")

    myImage = Image.open("Citi_bike_pic_1.jpeg")
    resized_image = myImage.resize((600, 400))
    st.image(resized_image)

### Weather component and bike usage page (dual-axis line chart)

elif page == "Weather component and bike usage":
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
        title = 'Daily bike trips and temperatures in New York 2022',
        height = 600
    )
    
    st.plotly_chart(fig_2, use_container_width=True)

    st.markdown("Seasonal Trend: Bike usage peaks in summer and drops significantly in colder months.")

    st.markdown("Temperature Correlation: There is a clear link between temperature and daily bike trips—lower temperatures lead to lower ridership. This confirms that weather is a primary factor influencing Citi Bike demand")

    st.markdown("Shortage Concern: Bike shortages are more likely during warmer months, roughly from May to October peaking during summer months June-September. ")

### Most popular stations page (top_20 bar chart)

elif page == "Most popular stations":

    with st.sidebar:
        season_filter = st.multiselect(label= 'Select the season', options=df['season'].unique(),
    default=df['season'].unique())

    df = df.query('season == @season_filter')
    
    # Define the total rides

    total_rides = float(df['bike_rides_daily'].count())    
    st.metric(label = 'Total Bike Rides', value= numerize(total_rides))

    df['value'] = 1 
    df_groupby_bar = df.groupby('start_station_name', as_index = False).agg({'value': 'sum'})
    
    top_20 = df_groupby_bar.nlargest(20, 'value')
    
    fig = go.Figure(go.Bar(x = top_20['start_station_name'], y = top_20['value']))
    
    fig = go.Figure(go.Bar(x = top_20['start_station_name'], y = top_20['value'], marker={'color': top_20['value'],'colorscale': 'Blues'}))
    fig.update_layout(
        title = 'Top 20 most popular bike stations in New York',
        xaxis_title = 'Start stations',
        yaxis_title ='Sum of trips',
        width = 900, height = 600
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Top 20 Bike Stations: The total number of bike rides for the top 20 stations is 298,000")

    st.markdown("Most Popular Stations: The most popular station is W 21 St & 6 Ave, recording the highest number of trips (~1,250). Other high-usage stations include West St & Chambers St, Broadway & W 58 St, and 1 Ave & E 60 St, each with over 1,000 trips. The distribution shows that several stations experience heavy ridership, likely in business districts and tourist hubs.")

    st.markdown("Popular Locations: Many high-traffic stations are near major avenues (e.g., Broadway, 6th Ave, 1st Ave), suggesting a strong commuter presence. Stations near parks (e.g., Central Park), transit hubs, and busy intersections see consistent usage.")

### Interactive map with aggregated bike trips page (Citi_bike Trips Aggregated)

elif page == "Interactive map with aggregated bike trips":

    ### Create the map ###

    st.write("Interactive map showing aggregated bike trips in New York 2022")

    path_to_html = "Citi_bike Trips Aggregated.html" 

    # Read file and keep in variable
    with open(path_to_html,'r') as f: 
        html_data = f.read()
    
    ## Show in webpage
    st.header("Aggregated Bike Trips in New York")
    st.components.v1.html(html_data,height=800, scrolling=True)

    st.markdown('#### Using the filter on the left hand side of the map, we can check whether the most popular start stations also appear in the most popular trips.')
    
    st.markdown("Central and lower Manhattan exhibit the highest trip densities, driven by their commercial significance and popularity among tourists. This trend is evident in the bike route from North Moore St & Greenwich St to Vesey St & Church St, which has recorded 4,523 trips. The starting station in TriBeCa is situated just a four-minute walk from the subway, making it highly accessible for both commuters and visitors in this vibrant neighborhood.")

    st.markdown("The end station at Vesey St & Church St sits near the Hudson River and the One World Observatory, a major landmark in downtown Manhattan. Church Street, despite its relatively short length, serves as a vital north-south corridor in lower Manhattan, experiencing significant traffic from cyclists, pedestrians, and vehicles.")

    st.markdown("Additionally, strong regional connectivity links Manhattan to Jersey City and Brooklyn, reinforcing the demand for cycling infrastructure. Certain key hubs dominate ridership, with some stations exceeding 500 trips, as highlighted by the color intensity in the interactive analysis. In contrast, northern Manhattan and peripheral areas exhibit lower trip activity.")

    st.markdown("With its dense population, high commuter traffic, and proximity to major attractions, the North Moore St & Greenwich St to Vesey St & Church St route is a prime example of how focused analysis can effectively highlight high-demand corridors and station usage patterns.")


elif page == "Recommendations":
    pass

    st.markdown("### Conclusions and Recommendations")

    myImage = Image.open("Citi_bike_pic_2.jpeg")
    resized_image = myImage.resize((600, 400))
    st.image(resized_image)

    st.markdown("### Our analysis underscores key areas for improvement in New York Citi Bike’s operations to enhance efficiency, accessibility, and user satisfaction. Moving forward, Citi Bike should prioritize the following strategies:")

    st.markdown("**Seasonal Demand Management** – Ridership increases with higher temperatures, peaking from **May through October**. To optimize operations:")

    st.markdown("- Maintain full station capacity during peak months while scaling back inventory by 20-30% in winter to reduce costs without compromising service.")
    st.markdown("- Monitor weather patterns to anticipate fluctuations and adjust bike availability dynamically.")
    st.markdown("- Pilot weather-resistant infrastructure to support year-round ridership.")

    st.markdown("**Enhancing Station Balancing & Redistribution** - Certain high-traffic stations, particularly in Central and Lower Manhattan (e.g., W 21 St & 6 Ave, West St & Chambers St, and Broadway & W 58 St), frequently experience supply-demand imbalances. To address this:")
    st.markdown("- Strengthen redistribution efforts and implement dynamic rebalancing strategies.")
    st.markdown("- Leverage real-time demand forecasting and predictive analytics to optimize bike distribution.")
    
    st.markdown("**Expanding High-Demand & Underserved Locations** - Stations along the waterfront and near Central Park consistently see higher usage, while some low-traffic areas remain underutilized. To improve accessibility and network efficiency:")
    st.markdown("Expand bike availability and parking capacity in high-demand zones.")
    st.markdown("Reallocate resources to better serve underserved regions and strengthen inter-borough connectivity.")
