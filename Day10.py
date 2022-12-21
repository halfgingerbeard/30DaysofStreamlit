# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:18:52 2022

@author: joshua.joy
"""

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue','Red','Green'))

st.write("Your favorite color is",option)