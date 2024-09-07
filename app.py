import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create a title for your app
st.title ('Machine Learning App')

# adding title for the app
st.header('Header')

# adding subheader to streamlit
st.subheader('Subheader')

# adding text to streamlit
st.text('Normal text')
st.markdown('Markdown text') 

# adding data to streamlit
data_dict = {'Course': ['Python', 'Machine Learning', 'Deep Learning', 'Data Science'],
             'Students': [100, 200, 150, 300],
             'Duration': [2, 3, 4, 6]}

df = pd.DataFrame(data_dict)
st.dataframe(df)


 # diabetes approximation model 
st.subheader('Diabetes Approximation Model')
# flamingo  
# rats
