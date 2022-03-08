# (C) Authors: 
#
# Professor Jian Chen
# Rui Li
# Isabel nekic
import streamlit as st
import pandas as pd
import random
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("CSE 5544 Lab 3")
st.markdown("### nekic.4")

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

#prepare the data
countries = data['Country\\year']
df_data_country = data.iloc[:,2:]
df_data_country = df_data_country.apply(pd.to_numeric, errors='coerce')
country_stats = pd.DataFrame({'country': countries, 'mean': df_data_country.mean(axis=1),
                       'std': df_data_country.std(axis=1)})

#render using altair
chart_data = data.drop(columns=['Non-OECD Economies'])
chart_data = pd.melt(chart_data, id_vars=['Country\year'], var_name='year')
chart_data['value'] = chart_data['value'].apply(pd.to_numeric, errors='coerce')
chart_data.rename(columns={"Country\year": "country", "value":"emission"}, inplace = True)
chart_data

heatmap = alt.Chart(chart_data).mark_rect().encode(
    x=alt.X('country:N', title = 'country'),
    y=alt.Y('year:O', title = 'year'),
    color='emission:Q',
    tooltip=['country', 'year', 'emission']
)

