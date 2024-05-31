import streamlit as st

st.title('Welcom to Streamlit tutorial')


st.header('Get number from user')
# For Number input 
input_val = st.number_input('Enter any number between 0-100',min_value=0, max_value=100, placeholder='Type a number...')
# if input_val.isnumeric() :
#     st.write('Please enter numbers only')
st.write(f'Your number {input_val}')

st.header('Get text from User')
input_text = st.text_input('Favorite Color',max_chars=10)
st.write(f'Your Favorite Color is {input_text}')