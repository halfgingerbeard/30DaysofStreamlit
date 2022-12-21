# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:54:04 2022

@author: joshua.joy
"""

import streamlit as st
import pandas as pd


st.header('emoji pattern :sunglasses:')

# load data
def load_data():
    df_emoji = pd.read_csv('emoji-dataframe.csv').iloc[1:,:]
    df_emoji.columns = ['index','shortcodes']
    return df_emoji

# create dataframe from function
df_emoji = load_data()

#select emoji to repeat

emoji1 = st.select_slider('Select emoji 1:', options = df_emoji['shortcodes'], value=':sunglasses:')
st.header(emoji1)
emoji2 = st.select_slider('Select emoji 2:', options = df_emoji['shortcodes'], value=':white_check_mark:')
st.header(emoji2)
emoji3 = st.select_slider('Select emoji 3:', options = df_emoji['shortcodes'], value=':coffee:')
st.header(emoji3)

# #select number of repetitions
e_columns = st.number_input('Select Number of Repetitions:',1,10,3)

st.write(emoji1, emoji2, emoji3)

repeat = (((emoji1, emoji2, emoji3) * e_columns)[:e_columns])
repeat




