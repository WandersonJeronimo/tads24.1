import streamlit as st
from functions.plot import plot_ts

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas listadas na B3.')

ticker = st.sidebar.text_input('Escolha o ticker:')
fig = plot_ts(ticker)
st.plotly_chart(fig)