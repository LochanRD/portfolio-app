import streamlit as st
import pandas as pd

st.title('Hello! I\'m Lochan.')

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('sources/professional_pic.jpeg', use_column_width=True)
    with col2:
        st.subheader('About Me')
        st.write('I\'m a data scientist with a passion for machine learning and data visualization.')

with st.container():
    st.subheader('My Projects')
    st.write('Here are some of the projects I have worked on:')
    st.write('1. [Project 1](https://www.example.com)')
    st.write('2. [Project 2](https://www.example.com)')