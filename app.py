import streamlit as st
import numpy as np
import pandas as pd

#Ttitle of the application
st.title("Hello World")

#Display a simple text
st.write("This is st.write to write a text")

#Display a DataFrame
df = pd.DataFrame({
    'first coloumn': [1, 2, 3], 
    'second couloumn': [3, 4, 6] })

st.write(df)

#Display a line chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)
