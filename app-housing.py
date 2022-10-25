import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Yerong Wu')
df = pd.read_csv('housing 2.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
median_housing_price_filter = st.slider('Minimum Median House Price:', 0, 500001, 200000) # min, max, default



# create a multi select
location_filter = st.sidebar.multiselect(
     'Lcation Selector',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a ratio button
level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Median', 'High'))

# filter by income
if level == 'Low':
    df = df[df.median_income <= 2.5]

elif level == 'Median':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]

elif level == 'High':
    df = df[df.median_income >= 4.5]


# filter by house value
df = df[df.median_house_value >= median_housing_price_filter]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(12, 8))
df['median_house_value'].plot.hist(bins=30)
st.pyplot(fig)