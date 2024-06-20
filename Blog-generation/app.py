import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers

# Blog generation code


st.set_page_config(page_title='Blog Generation',
                   page_icon=':robot_face:',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header('Blog Generation :robot_face: ')

input_text =st.text_input('Enter The Blog Topic')

col1, col2 = st.columns([5,5])
# columns types
with col1:
    no_words = st.text_input('No of words')
with col2:
    blog_style = st.selectbox('Writing blog for',("Data science", "Researcher", "Common Man"),index=2)

# add button 
submit = st.button('submit')


