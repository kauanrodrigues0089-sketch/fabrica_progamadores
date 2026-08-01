#autor:kauan pietro

try:
    celsius = float(input("Digite a temperatura em graus celsius : "))
    fahrenheit =(celsius*(9/5))+32


    print(f' {celsius} equivalem a { fahrenheit:.2f}')
except:
    print("Digite apenas nú