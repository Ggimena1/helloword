import streamlit as st 
import altair as alt
import pandas as pd
import numpy as np

st.write('LAVADOS')
st.header('st.button')
if st.button ('Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
st.header('st.write')
# ejemplo 1
st.write('HELLO, *CONSULTA DE LAVADOS!* :sunglasses:')
#ejemplo 2
st.write(1234)

#ejemplo 3
df = pd.DataFrame ({
    'first column':[1, 2, 3, 4],
    'second column':[10, 20, 30, 40]
    })
st.write(df)

#ejemplo 4
st.write('Below is a DataFreme:', df, 'above is a datafreme.')

#ejemplo 5 muestra graficos y se representan en circulos
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a','b','c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='b', tooltip=['a', 'b','c'])
st.write(c)
