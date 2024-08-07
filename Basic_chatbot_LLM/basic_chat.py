
from transformers import pipeline


# create question-answering pipeline
# if we didn't provide model name then by defaul it will select distilbert-base-cased-distilled-squad
qa = pipeline('question-answering') 

context = 'Jeremy likes apple macbook pro laptop and he dont like to eat apple. '
question= 'what Jeremy dont likes?'
result= qa(context= context, question= question)

print(result)
print('Answer: ', result['answer'])

