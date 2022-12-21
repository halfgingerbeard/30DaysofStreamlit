# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 13:00:51 2022

@author: joshua.joy
"""

import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

st.line_chart(chart_data)
