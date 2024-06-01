import pandas as pd
import numpy as np
import streamlit as st

st.title('Plot graph on Streamlit')

plot_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['col_a', 'col_b', 'col_c']
)

# print(plot_data)
st.bar_chart(plot_data)
st.line_chart(plot_data)

st.link_button('profile', url="/profile")
st.link_button('Dashboard', url ='/dashboard')