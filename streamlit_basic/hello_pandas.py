# we will read csv file using pandas, 
# show the graphs on website using steamlit

import pandas as pd
import streamlit as st

st.title('Show datafram in Streamlit')

df = pd.read_csv('data/olist_customers_dataset.csv', nrows=10)
print(df.head())
st.write(df)


