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

st.header("P1: Honest/Ethical/Truthful")

