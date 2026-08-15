# Autor:Kauan Pietro
# Projeto:minha primeira pagina web

# importando a biblioteca
import streamlit as st

st.title('---sistema do calculo de IMC...')
peso = st.number_input('digite seu peso: ')
altura = st.number_input('digite sua altura: ')
if st.button('calcular IMC'):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.success(f'Seu IMC é: {imc}', icon="✅")
        if imc <= 18.5:
            st.error('Abaixo do peso', icon="🚨")
        elif imc <= 24.9:
            st.success('peso normal', icon="✅")
        elif imc <= 29.9:
            st.warning('Sobrepeso', icon="⚠️")
        elif imc <= 34.9:
            st.warning('Obesidade grau I', icon="⚠️")
        elif imc <= 39.9:
            st.warning('Obesidade grau II', icon="⚠️")
        else:
             st.error('Obesidade grau III (mórbida)', icon="🚨")
    else:
        st.error('Digite um número valído', icon="🚨")