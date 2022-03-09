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

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

# Beginning of P1
st.markdown("### P1: Honest/Ethical/Truthful")
st.markdown("##### Source: https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG")

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
"The wide range of colors in the rainbow palette allows the viewer to more clearly see the slight differences in emissions."
"The separation between data values in P1 is maintained, allowing a clear interpretation of the visualization."
"Blank spaces show where there was no data recorded for that year in that country." 
"The titles for P1 are clear and helpful. The color bar is included and labeled."
"The climate data source is listed."

st.markdown("##### P2")
"The visualization for P2 is misleading."
"The color palette makes it very hard to distinguish slight emission differences due to the darker colors.
"The border separating the different data points was removed, making it much harder to read the data, as it is difficult for the viewer to distinguish between different data points."
"The data was incorrectly cleaned and missing data were replaced with a 0, which shows on the heatmap as there being 0 emissions for that country and year."
"The titles for P2 are either missing or vague. The color bar showing the emission values to color relationship is missing and the viewer can only guess what the different colors mean. "
"There is no listed source in P2."
