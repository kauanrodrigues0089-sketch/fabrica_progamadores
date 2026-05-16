# Autor:Kauan Pietro
# Projeto:condicionais
# Definicao variaveis
nome=input('Digite seu nome: ')
idade = int (input ('Digite sua idade: '))
produto = int(input('Digite o preco do produto'))
if produto >=100:
    produto = produto * 0.95
    print('esta caro')
else:
    produto = produto * 0.90
    print('esta barato')