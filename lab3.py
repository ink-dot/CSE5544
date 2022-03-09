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

# Title and header
st.title("CSE 5544 Lab 3")
st.markdown("### nekic.4")

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

# Beginning of P1
st.header("## P1: Honest/Ethical/Truthful")

df_data1 = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data1.T, linewidths=.5, cmap='rainbow', cbar_kws={'label': 'Emissions in Tons of C02'})
ax.set_xlabel('Country')
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Heatmap of Emissions of Countries over Years')

st.pyplot(fig)

# Beginning of P2
st.header(## "P2: Dishonest/Unethical/Misleading")

df_data2 = data.apply(pd.to_numeric, errors='coerce')
df_data2.fillna(0, inplace=True)

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data2.T, cmap='inferno', cbar=False)
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Emissions')

st.pyplot(fig)

# Write Up
st.header("## Write Up")
"The visualization for P1 is better."
"This is because P1 is an accurate and truthful representation of the data. The wide range of colors in the rainbow palette allows the viewer to more clearly see the slight differences in emissions, whereas the color palette in P2 makes it very hard to distinguish between the darker colors.
"The border separating the different data points was removed in P2. This makes it much harder to read the data, as it is difficult for the viewer to distinguish between different data points. The separation between data values in P1 is maintained and the visualization is easier to interpret.
"For P1, blank spaces show where there was no data recorded for that year in that country. For P2, however, missing data was replaced with a 0, which shows on the heatmap as there being 0 emissions for that country and year. This is very misleading, as it implies that emissions for countries with missing data are much lower than they might be. This is especially relevant in regards to China. China has very high emissions for the 5 recorded years, but appears to overall have low emissions in the P2 heatmap because the missing years have been filled in with 0s, even though it is impossible for China to have had 0 emissions in those unrecorded years. By leaving the missing data as NaN, P1 allows a more straightforward and truthful reading of the data than P2.
"The titles for P2 are either missing or vague. The color bar showing the emission values to color relationship is missing. The viewer can only guess what the different colors mean. The titles for P1 are clear and helpful. The color bar is included and labeled.
