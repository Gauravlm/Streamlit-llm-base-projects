import pandas as pd
import streamlit as st
from io import StringIO


upload_file = st.file_uploader('choose a file')
st.write('filename: ', upload_file.name)

if upload_file is not None:
    st.title('uploaded data')
    get_data = upload_file.getvalue()
    st.write(get_data)

    st.title('Stringio utf-8 decoded data')
    stringio = StringIO(upload_file.getvalue().decode('utf-8'))
    st.write(stringio)

    st.title('string_data')
    string_data = stringio.read()
    st.write(string_data)

    st.title('Dataframe')
    dataframe = pd.read_csv(upload_file)
    st.write(dataframe)


