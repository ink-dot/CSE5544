import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

st.title("CSE 5544 Lab 3")
st.markdown("### nekic.4")

st.header("Climate Data")

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

#prepare the data
countries = data['Country\\year']
df_data_country = data.iloc[:,2:]
df_data_country = df_data_country.apply(pd.to_numeric, errors='coerce')
country_stats = pd.DataFrame({'country': countries, 'mean': df_data_country.mean(axis=1),
                       'std': df_data_country.std(axis=1)})

#heatmap
fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data_country.T, linewidths=.5, cmap='flare_r')

ax.set_xlabel('Country')
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Heatmap of Emissions of Countries over Years')


