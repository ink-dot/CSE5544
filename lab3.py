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

df_data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")
df_data.columns = df_data.iloc[0]
df_data.drop(df_data.index[0], inplace=True)

df_data.set_index('Country\year', inplace=True)
df_data = df_data.drop(columns=['Non-OECD Economies'])
df_data.drop(index='OECD - Total', inplace=True)
df_data.reset_index(inplace=True)

countries = df_data['Country\year']
emissions = df_data.iloc[:,1:]
emissions = emissions.apply(pd.to_numeric, errors='coerce')

stats = pd.DataFrame({'total' : emissions.sum(), 'mean': emissions.mean(),'std': emissions.std()})
total = emissions.sum(axis=1)
mean = emissions.mean(axis=1)
std = emissions.std(axis=1)

st.header("P1: Honest/Ethical/Truthful")

df_data1 = df_data.apply(pd.to_numeric, errors='coerce')

fig, ax = plt.subplots(figsize=(20, 10))
ax = sns.heatmap(df_data1.T, linewidths=.5, cmap='rainbow', cbar_kws={'label': 'Emissions in Tons of C02'})

ax.set_xlabel('Country')
ylabel = ax.set_ylabel('Year')
xaxis = plt.xticks(rotation=90, ha='center', fontsize=8)
title = ax.set_title('Heatmap of Emissions of Countries over Years')
