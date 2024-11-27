# **Citi_bike Analysis**
### **Data and Tools** 
#### This project used open sourced data from the Citi Bike database for year 2022 and weather data from NOAA's API service.  I used Python libraries, including Matplotlib, Seaborn, and Plotly to make charts; pandas and Kepler.gl to create maps; and Streamlit to design my final dashboard.
### **Introduction**
####  Citi Bike is a bike-sharing service based in New York City.  The objective is to analyze user behavior to help the business strategy department and assess the current logistics model of bike distribution across the city and identify expansion opportunities.  The project’s objective is to conduct a descriptive analysis of existing data and discover actionable insights for the business strategy team to help make informed decisions that will circumvent availability issues and ensure the company’s position as a leader in eco-friendly transportation solutions in the city. 
### **Analysis Criteria**
####  Use descriptive analysis and apply aggregations of bike trips across New York to discover the most popular starting locations and summarize data yearly to find seasonal patterns.  Apply geographic plotting to identify problem areas in station distribution and explore the most common routes.
### **Visualization Criteria**
####  Develop a Python-based dashboard to present the findings of my analysis effectively. Structure the dashboard into sections that focus on the variables influencing demand. Ensure that each graph is visually engaging, using a refined color palette to enhance clarity and aesthetics. The dashboard should include the following:
####  **Introduction**: Provide context and set the stage for the presentation.
####  **Individual Graph Slides**: Display one graph per slide to maintain focus and avoid overwhelming the audience.
####  **Recommendations Page**: Conclude with a clear and concise summary of the analysis outcomes, along with actionable recommendations.
####  This structured approach will ensure a polished and audience-friendly presentation.
### **Success Factors**
####   Present an interactive dashboard that depicts all the problematic aspects of bike logistics around the city.  The dashboard contains visualizations that seek to understand the different factors that
could affect the business, accompanied with strategy recommendations and next steps based on your findings.
### **Dashoboard Elements**
####  Bar Chart
####  Line Chart
####  Map
###  **Data Analysis Questions and dashboard elements**
####  List of elements for dashboard:
####  Q1: Bar Chart
####  Q2: Line Chart
####  Q3 and Q4: Map
###  Question 1: Which stations are the most popular in the city?
I need to identify the 10-20 most popular stations in New York. A bar chart would be ideal since the data is categorical, making it the most suitable visualization.  I would use a multi color scheme, so each bar/station has its own unique color with station names on the X axis and number of trips on the Y axis.
###  Question 2:  During which months are the most trips taken? Is there a correlation with weather conditions?
I’ll need to show a month-by-month overview of trips taken throughout the year. A line chart is appropriate for this time series data, allowing me to plot the number of trips per month alongside average monthly temperature and the number of bikes in use. The line chart will have a blue line and the charts X axis will represent the months of the year (January to December) and the Y axis would represent the number of trips.  The second line chart will be a green line which will represent the avg monthly temperature.  
###  Question 3:  What are the most popular trips between stations? 
###  Question 4:  Are the stations distributed evenly throughout the city?
### **(Please see answers to both questions below)**
I need to identify the busiest areas in the city, which will assist in managing bike shortages in specific regions. I also need to show if stations are distributed evenly throughout the city.  A map is suitable for visualizing geographic data, plotting the most common bike routes with aggregation to differentiate one-time trips from recurring ones.  Trip density can be represented by using heatmaps or choropleth layers with gradients of color intensity indicating areas with high or low trip activity.  For layer styling I can use contrasting color schemes to distinguish trip density such as a warm color like red-yellow and for station distribution use cool tones or icon markers. I’ll also add a clear legend to help users interpret the data accurately.  For interactivity features I can use tooltips/pop-ups to display information such as station names, trip counts, or capacity when hovering over or clicking station markers. Since both questions will be answered utilizing the same map, I can use layer toggles to enable toggling between trip density and station distribution layers or viewing bot simultaneously. Filters and time ranges will be added to let users filter trips by time, date, or type such as peak hours vs off peak hours to analyze temporal trends.

