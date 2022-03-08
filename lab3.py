# (C) Authors: 
#
# Professor Jian Chen
# Rui Li
# Isabel nekic
import pandas as pd
import random
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm, Normalize
from matplotlib.ticker import MaxNLocator

st.title("CSE 5544 Lab 3")
st.markdown("### nekic.4")

st.header("Climate Data")

df_data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

# make row 0 into the column headers, then drop it
df_data.columns = df_data.iloc[0]
df_data.drop(df_data.index[0], inplace=True)


