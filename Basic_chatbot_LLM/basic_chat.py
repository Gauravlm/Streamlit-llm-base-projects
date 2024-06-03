import streamlit as st 

# with st.chat_message('User'):
#     st.write('Hello 🤚')

chat_input= st.chat_input('Say something')
st.write(f'User: ',chat_input)