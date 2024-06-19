'''
Chat bot using Streamlit 
Model name: distilbert-base-cased-distilled-squad ( by default)
'''

import streamlit as st 
from transformers import pipeline

# with st.chat_message('User'):
#     st.write('Hello 🤚')

st.title('Basic chatbot')

context= st.chat_input('Give Me context')
st.write(f'User: ',context)
qa = pipeline('question-answering') 
question = st.chat_input('Ask me any question based on give context.')
st.write(question)
# create question-answering pipeline
# if we didn't provide model name then by defaul it will select distlibert


# context = 'Jeremy likes apple macbook pro but he dont like to eat apple fruit. '
# question= 'what Jeremy dont liks?'
if question : 
    result= qa(context= context, question= question)
    st.write(f'Answer: {result["answer"]}')

        