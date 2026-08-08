#Autor:kauan pietro
#projeto:trabalhando com arquivos

nome = input('digite seu nome:')
email = input('digite seu email:')

arquivo = open('agenda.txt','a')
arquivo.write(nome + ' | '+ email +'/n')
arquivo.close()