# (C) Authors: 
#
# Professor Jian Chen
# Rui Li
# Isabel nekic
#
# Contains code from Lab 1 solutions
#
# 2022 Spring: For The Ohio State University, Intro. Data. Vis Lectures
# 
# import libraries
# Click the arrow in the upper left corner. You will get the line like this
# "Go to the following link in your browser" following by a blue link or a weblink.
# click that link, choose your google account to authorize, and accept to obtain
# an access code. Use the icon (like two squares) to copy the code and paste to the 
#  "Enter verification code:" - AND hit character return (from your keyboard)
# 
import pandas as pd
import random
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm, Normalize
from matplotlib.ticker import MaxNLocator

# Import the library, authenticate, and create the interface to Sheets.
# https://colab.research.google.com/notebooks/io.ipynb?hl=en#scrollTo=sOm9PFrT8mGG
from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

# access the google sheet and load it into pandas dataframe
#################### Do this only at the first time
wkbook = 'https://docs.google.com/spreadsheets/d/1HiVAuTr1miXHKCmxRDu_ZspUXttlRINN3ec2CvFHg1k/edit?usp=sharing'

wb = gc.open_by_url(wkbook)
sheet = wb.worksheet('Sheet1')
sheet_data = sheet.get_all_values()

df_data = pd.DataFrame(sheet_data)
# make row 0 into the column headers, then drop it
df_data.columns = df_data.iloc[0]
df_data.drop(df_data.index[0], inplace=True)


st.title("CSE 5544 Lab 3")
st.markdown("### nekic.4")

st.header("Climate Data")

data = pd.read_csv("https://raw.githubusercontent.com/ink-dot/CSE5544/main/CSE5544.Lab1.ClimateData%20-%20Sheet1.csv")

