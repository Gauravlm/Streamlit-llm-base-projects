'''
Task for model
Step 1: Read PDF
Step 2: divide text into chunks like 1000 
step 3: Embedding for each chunks --> used FAISS ( to vectorize our chunk)

Tast for Streamlit
1. Preserve chat history
'''
from src.model import *
from transformers import pipeline
import streamlit as st

from transformers import TFDistilBertForQuestionAnswering,DistilBertTokenizer
from PyPDF2 import pdfReader


def get_text_pdf(pdf_files):
    text=''
    for pdf_file in pdf_files:
        reader = pdfReader(pdf_file)
        for page in reader.pages():
            text += page.extract_text()

    return text

model_name = 'distilbert-base-uncased-distilled-squad'
model = TFDistilBertForQuestionAnswering.from_pretrained(model_name)
tokenizer = DistilBertTokenizer.from_pretrained(model)

# model.save_pretrained('/custom_model/')
# tokenizer.save_pretrained('/custom_model/')


# load finetune  model

# qa_pipeline = pipeline('question-answering', model='/custom_model', tokenizer='/custom_model')

# steeamlit interface
# st.title('PDF Quesiton Answering bot')

# upload_file = st.file_uploader('Choose a PDF file ', type='pdf')

# if upload_file is not None:
#     pdf_path = upload_file.name
#     with open(pdf_path, 'wb') as f:
#         f.write(upload_file.getbuffer())

#     text = get_text_pdf(pdf_path)
#     st.write('PDF content extacted Succesfully !')

#     question = st.text_input('Ask question abou PDF: ')
#     if question:
#         result = qa_pipeline(question=question, context = text)
#         st.write(f'Answer: {result["answer"]}')