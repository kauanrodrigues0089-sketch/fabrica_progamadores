# Autor:kauan pietro
# projeto:entendendo tratamento de exceção
try:
    valor1 = float(input('digite o primeiro valor'))
    valor2 = float(input('digite o primeiro valor'))
    soma = valor1+valor2
    print(f'o resultado da soma é: {soma}')
except:
    print('digite apenas numeros')