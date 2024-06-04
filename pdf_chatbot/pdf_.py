'''
Task for model
Step 1: Read PDF
Step 2: divide text into chunks like 1000 
step 3: Embedding for each chunks --> used FAISS ( to vectorize our chunk)

Tast for Streamlit
1. Preserve chat history
'''

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, Trainer, TrainingArguments

from PyPDF2 import pdfReader


def get_text_pdf(pdf_files):
    text=''
    for pdf_file in pdf_files:
        reader = pdfReader(pdf_file)
        for page in reader.pages():
            text += page.extract_text()

    return text

model_name = 'distilbert-base-uncased-distilled-squad'
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model)

model.save_pretrained('./custom_model')
tokenizer.save_pretrained('./custom_model')

