# Autor:Kauan Pietro
# Projeto:condicionais
# Definicao variaveis
nome=input('Digite seu nome: ')
peso = int(input('Digite seu peso'))
altura = int(input('Digite sua altura'))
IMC = peso / (altura*altura)
if IMC >= 18.85:
    print('voce esta abaixo do peso')
else:
    print('peso normal')