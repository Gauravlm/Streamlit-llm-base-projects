import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Blog generation code
def getllamaresponse(input_text, no_words, blog_style):

    # load model using ctransfromers
    # CTransfromers provide binding for ggml model 
    # to get below model link:- https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
    model = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                          model_type='llama',
                          config={'max_new_tokens':256,
                                  'temperature':0.01 })
    # create template 
    template = """ write blog for {blog_style} job proflie for topic{input_text} """ #withing {no_words} words

    prompt = PromptTemplate(input_variables=['blog_style','input_text'], # ,'no_words'
                            template=template)
    
    # get response
    response = model(prompt.format(blog_style = blog_style,
                                   input_text=input_text,
                                   #no_words= no_words
                                   ))
    print(response)
    return response
    

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

if submit:
    # write model response
    st.write(getllamaresponse(input_text, no_words, blog_style))
    


