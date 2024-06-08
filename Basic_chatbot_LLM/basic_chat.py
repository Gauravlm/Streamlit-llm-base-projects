import streamlit as st 

# with st.chat_message('User'):
#     st.write('Hello 🤚')

chat_input= st.chat_input('Say something')
st.write(f'User: ',chat_input)


upload_file = st.file_uploader('Choose a PDF file', type='pdf')

if upload_file is not None:
    pdf_path = upload_file.name
    with open(pdf_path, 'wb') as f:
        f.write(upload_file.getbuffer())
        