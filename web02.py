import streamlit as st

st.title('---Programa para geracao de preco')
produto = st.number_input('Entre com o produto')
mao_de_obra= st.number_input('custo da mao de obra')
energia = st.number_input('custo da energia')
internet = st.number_input('custo da internet')
agua = st.number_input('custo da agua')
imposto =st.number_input('custo do imposto') 
lucro = st.number_input('lucro')
if st.button('calcular preco de venda'):
    preco = produto + mao_de_obra + energia + internet + agua('produto * 0,02')
    st.write(f'o preco é')