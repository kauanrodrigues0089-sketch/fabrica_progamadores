#autor:kauan pietro 

try:
    reais = float(input("Digite o valor em reais: "))
    cotacao = float(input("Digite a cotação do dólar: "))

    dolares = reais / cotacao

    print(f' {reais} equivalem a {dolares:.2f}')
except:
    print("Digite apenas números.")
# calcular o IMC usando a formula:peso/(altura ao quadrado)
def calcular(peso,altura):
    imc = peso/(altura**2)
    print(f'seu IMC é :(imc)')

calcular(peso,altura)