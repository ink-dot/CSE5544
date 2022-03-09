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


df_data1 = data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data1.T, linewidths=.5, cmap='rainbow', cbar_kws={'label': 'Emissions in Tons of C02'})

ax.set_xlabel('Country')
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Heatmap of Emissions of Countries over Years')


st.header("P1: Honest/Ethical/Truthful")

