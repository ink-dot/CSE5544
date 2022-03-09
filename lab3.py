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
st.markdown("##### nekic.4")
st.markdown("##### Link to Github code: https://github.com/ink-dot/CSE5544/edit/main/lab3.py")

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

# Beginning of P1
st.markdown("### P1: Honest/Ethical/Truthful")
st.markdown("##### Source: https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG")

data.set_index('Country\year', inplace=True)
data = data.drop(columns=['Non-OECD Economies'])
data.drop(index='OECD - Total', inplace=True)
data.reset_index(inplace=True)

df_data1 = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data1.T, linewidths=.5, cmap='rainbow', cbar_kws={'label': 'Emissions in Tons of C02'})
ax.set_xlabel('Country')
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Heatmap of Emissions of Countries over Years')

st.pyplot(fig)

# Beginning of P2
st.markdown("### P2: Dishonest/Unethical/Misleading")

df_data2 = data.apply(pd.to_numeric, errors='coerce')
df_data2.fillna(0, inplace=True)

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data2.T, cmap='inferno', cbar=False)
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Emissions')

st.pyplot(fig)

# Write Up
st.markdown("### Write Up")
st.markdown("##### P1")
"The visualization for P1 is the better heatmap."
"The wide range of colors in the rainbow palette, in addition to the separation between data values allows a clear interpretation of the visualization."
"The visualization is transparent -- missing data points are clearly displayed and the climate data source is listed." 
"The titles for P1 are clear and helpful. The color bar is included and labeled."

st.markdown("##### P2")
"The visualization for P2 is misleading."
"The visualization is hard to interpret, as the color palette makes it very hard to distinguish slight differences in emission, along with the fact that the border separating the different data points was removed."
"In addition, the data is misleading as it was incorrectly cleaned, with missing data being unethically replaced with a 0 along with no listed source for the emissions data."
"The titles are either missing or vague. The color bar showing the emission values to color relationship is missing and the viewer can only guess what the different colors mean."
