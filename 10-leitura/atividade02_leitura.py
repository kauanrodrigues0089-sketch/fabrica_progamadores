#autor:kauan pietro
#trabalhando com arquivo

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')

carga_horaria = 200
valor_hora = 22.22
salario = carga_horaria * valor_hora

arquivo = open('funcionario.txt', 'a')
arquivo.write(f'{nome} | {email} | {telefone} | {salario:.2f}\n')
arquivo.close()